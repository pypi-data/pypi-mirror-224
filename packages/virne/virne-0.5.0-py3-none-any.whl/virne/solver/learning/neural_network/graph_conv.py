from typing import Any, Callable, Dict, List, Optional, Union

import torch
from torch import Tensor
import torch.nn.functional as F
from torch.nn import Parameter, ModuleList, Sequential, ReLU
from typing import Optional, Tuple, Union, Callable
from torch_sparse import SparseTensor, set_diag
from torch_geometric.nn.conv import MessagePassing
from torch_geometric.nn.dense.linear import Linear
from torch_geometric.typing import (Adj, NoneType, OptPairTensor, OptTensor, Size)
from torch_geometric.utils import add_self_loops, remove_self_loops, softmax
from torch_geometric.nn.inits import glorot, zeros
from torch_geometric.nn.inits import reset, zeros
from torch_geometric.typing import Adj, OptPairTensor, OptTensor, Size


class EdgeFusionGATConv(MessagePassing):
    """
    The graph attentional operator from the Graph Attention Networks
    <https://arxiv.org/abs/1710.10903>`_ paper
    """
    _alpha: OptTensor

    def __init__(
        self,
        in_channels: Union[int, Tuple[int, int]],
        out_channels: int,
        heads: int = 1,
        concat: bool = True,
        negative_slope: float = 0.2,
        dropout: float = 0.0,
        add_self_loops: bool = True,
        edge_dim: Optional[int] = None,
        fill_value: Union[float, Tensor, str] = 'mean',
        bias: bool = True,
        **kwargs,
    ):
        kwargs.setdefault('aggr', 'add')
        super(EdgeFusionGATConv, self).__init__(node_dim=0, **kwargs)

        self.in_channels = in_channels
        self.out_channels = out_channels
        self.heads = heads
        self.concat = concat
        self.negative_slope = negative_slope
        self.dropout = dropout
        self.add_self_loops = add_self_loops
        self.edge_dim = edge_dim
        self.fill_value = fill_value

        self.F_in = out_channels

        self.pre_nns = ModuleList()
        modules = [Linear((3 if edge_dim else 2) * self.F_in, self.F_in)]
        for _ in range(1):
            modules += [ReLU()]
            modules += [Linear(self.F_in, self.F_in)]
        self.pre_nns.append(Sequential(*modules))

        # In case we are operating in bipartite graphs, we apply separate
        # transformations 'lin_src' and 'lin_dst' to source and target nodes:
        if isinstance(in_channels, int):
            self.lin_src = Linear(in_channels, heads * out_channels,
                                  bias=False, weight_initializer='glorot')
            self.lin_dst = self.lin_src
        else:
            self.lin_src = Linear(in_channels[0], heads * out_channels, False,
                                  weight_initializer='glorot')
            self.lin_dst = Linear(in_channels[1], heads * out_channels, False,
                                  weight_initializer='glorot')

        # The learnable parameters to compute attention coefficients:
        # self.att_src = Parameter(torch.Tensor(1, heads, out_channels))
        # self.att_dst = Parameter(torch.Tensor(1, heads, out_channels))

        if edge_dim is not None:
            self.lin_edge = Linear(edge_dim, heads * out_channels, bias=False,
                                   weight_initializer='glorot')
            # self.att_edge = Parameter(torch.Tensor(1, heads, out_channels))
            self.register_parameter('att_edge', None)
        else:
            self.lin_edge = None
            self.register_parameter('att_edge', None)

        if bias and concat:
            self.bias = Parameter(torch.Tensor(heads * out_channels))
        elif bias and not concat:
            self.bias = Parameter(torch.Tensor(out_channels))
        else:
            self.register_parameter('bias', None)

        self._alpha = None

        self.reset_parameters()

    def reset_parameters(self):
        self.lin_src.reset_parameters()
        self.lin_dst.reset_parameters()
        if self.lin_edge is not None:
            self.lin_edge.reset_parameters()
        for nn in self.pre_nns:
            reset(nn)
        # glorot(self.att_src)
        # glorot(self.att_dst)
        # glorot(self.att_edge)
        zeros(self.bias)

    def forward(self, x: Union[Tensor, OptPairTensor], edge_index: Adj,
                edge_attr: OptTensor = None, size: Size = None,
                return_attention_weights=None):
        # type: (Union[Tensor, OptPairTensor], Tensor, OptTensor, Size, NoneType) -> Tensor  # noqa
        # type: (Union[Tensor, OptPairTensor], SparseTensor, OptTensor, Size, NoneType) -> Tensor  # noqa
        # type: (Union[Tensor, OptPairTensor], Tensor, OptTensor, Size, bool) -> Tuple[Tensor, Tuple[Tensor, Tensor]]  # noqa
        # type: (Union[Tensor, OptPairTensor], SparseTensor, OptTensor, Size, bool) -> Tuple[Tensor, SparseTensor]  # noqa
        """
        Args:
            return_attention_weights (bool, optional): If set to :obj:`True`,
                will additionally return the tuple
                :obj:`(edge_index, attention_weights)`, holding the computed
                attention weights for each edge. (default: :obj:`None`)
        """
        # NOTE: attention weights will be returned whenever
        # `return_attention_weights` is set to a value, regardless of its
        # actual value (might be `True` or `False`). This is a current somewhat
        # hacky workaround to allow for TorchScript support via the
        # `torch.jit._overload` decorator, as we can only change the output
        # arguments conditioned on type (`None` or `bool`), not based on its
        # actual value.

        H, C = self.heads, self.out_channels

        # We first transform the input node features. If a tuple is passed, we
        # transform source and target node features via separate weights:
        if isinstance(x, Tensor):
            assert x.dim() == 2, "Static graphs not supported in 'GATConv'"
            x_src = x_dst = self.lin_src(x).view(-1, H, C)
        else:  # Tuple of source and target node features:
            x_src, x_dst = x
            assert x_src.dim() == 2, "Static graphs not supported in 'GATConv'"
            x_src = self.lin_src(x_src).view(-1, H, C)
            if x_dst is not None:
                x_dst = self.lin_dst(x_dst).view(-1, H, C)

        x = (x_src, x_dst)

        # Next, we compute node-level attention coefficients, both for source
        # and target nodes (if present):
        # alpha_src = (x_src * self.att_src).sum(dim=-1)
        # alpha_dst = None if x_dst is None else (x_dst * self.att_dst).sum(-1)
        # alpha = (alpha_src, alpha_dst)

        if self.add_self_loops:
            if isinstance(edge_index, Tensor):
                # We only want to add self-loops for nodes that appear both as
                # source and target nodes:
                num_nodes = x_src.size(0)
                if x_dst is not None:
                    num_nodes = min(num_nodes, x_dst.size(0))
                num_nodes = min(size) if size is not None else num_nodes
                edge_index, edge_attr = remove_self_loops(
                    edge_index, edge_attr)
                edge_index, edge_attr = add_self_loops(
                    edge_index, edge_attr, fill_value=self.fill_value,
                    num_nodes=num_nodes)
            elif isinstance(edge_index, SparseTensor):
                if self.edge_dim is None:
                    edge_index = set_diag(edge_index)
                else:
                    raise NotImplementedError(
                        "The usage of 'edge_attr' and 'add_self_loops' "
                        "simultaneously is currently not yet supported for "
                        "'edge_index' in a 'SparseTensor' form")


        alpha = self._alpha = None

        # propagate_type: (x: OptPairTensor, alpha: OptPairTensor, edge_attr: OptTensor)  # noqa
        out = self.propagate(edge_index, x=x, alpha=None, edge_attr=edge_attr,
                             size=size)

        # alpha = self._alpha
        # assert alpha is not None
        # self._alpha = None

        if self.concat:
            out = out.view(-1, self.heads * self.out_channels)
        else:
            out = out.mean(dim=1)

        if self.bias is not None:
            out += self.bias

        if isinstance(return_attention_weights, bool):
            if isinstance(edge_index, Tensor):
                return out, (edge_index, alpha)
            elif isinstance(edge_index, SparseTensor):
                return out, edge_index.set_value(alpha, layout='coo')
        else:
            return out

    def message(self, x_i: Tensor, x_j: Tensor, alpha_j: Tensor, alpha_i: OptTensor,
                edge_attr: OptTensor, index: Tensor, ptr: OptTensor,
                size_i: Optional[int]) -> Tensor:
        # Given edge-level attention coefficients for source and target nodes,
        # we simply need to sum them up to "emulate" concatenation:
        # alpha = alpha_j if alpha_i is None else alpha_j + alpha_i

        # if edge_attr is not None:
        #     if edge_attr.dim() == 1:
        #         edge_attr = edge_attr.view(-1, 1)
        #     assert self.lin_edge is not None
        #     raw_edge_attr = self.lin_edge(edge_attr)
        #     edge_attr = raw_edge_attr.view(-1, self.heads, self.out_channels)
        #     alpha_edge = (edge_attr * self.att_edge).sum(dim=-1)
        #     alpha = alpha + alpha_edge

        # alpha = F.leaky_relu(alpha, self.negative_slope)
        # alpha = softmax(alpha, index, ptr, size_i)
        # self._alpha = alpha  # Save for later use.
        # alpha = F.dropout(alpha, p=self.dropout, training=self.training)

        h: Tensor = x_i  # Dummy.
        if edge_attr is not None:
            edge_embedding = self.lin_edge(edge_attr)
            h_edge_attr = edge_embedding.view(-1, 1, self.F_in)
            h = torch.cat([x_i, x_j, h_edge_attr], dim=-1)
        else:
            h = torch.cat([x_i, x_j], dim=-1)

        hs = [nn(h[:, i]) for i, nn in enumerate(self.pre_nns)]
        new_x_j = torch.stack(hs, dim=1)
        # new_x_j * alpha.unsqueeze(-1) * alpha.unsqueeze(-1)
        return new_x_j

    def __repr__(self) -> str:
        return (f'{self.__class__.__name__}({self.in_channels}, '
                f'{self.out_channels}, heads={self.heads})')
