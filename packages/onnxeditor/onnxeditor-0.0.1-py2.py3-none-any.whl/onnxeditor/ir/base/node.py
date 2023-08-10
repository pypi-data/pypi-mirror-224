from typing import TYPE_CHECKING, List, Dict, Any
from .obj import IRObj
import json
import numpy as np
import copy

if TYPE_CHECKING:
    from .graph import Graph
    from .variable import Variable


class Node(IRObj):
    def __init__(self, graph: 'Graph', name: str, op_type: str) -> None:
        super().__init__()

        self.name: str = name
        self.op_type: str = op_type
        self.domain: str = None
        self.doc_string: str = None
        self._attrs: Dict[str: Any] = {}
        self._input: List[str] = []
        self._output: List[str] = []

        self._graph: 'Graph' = graph

        self.displayAttr('name')
        self.displayAttr('op_type')
        self.displayAttr('domain')
        self.displayAttr('doc_string')
        self.displayAttr('attrs')
        self.displayAttr('_input', name='input')
        self.displayAttr('_output', name='output')

    @property
    def input(self):
        return [self._graph.getVariable(v) for v in self._input]

    @input.setter
    def input(self, new_ins):
        new_ins = [self._graph.getVariable(v) if isinstance(
            v, str) else v for v in new_ins]
        old_ins = [self._graph.getVariable(v) for v in self._input]
        self._input = [v.name for v in new_ins]
        old_ins = set([v.name for v in old_ins])
        new_ins = set([v.name for v in new_ins])
        diff_old_ins = old_ins - new_ins
        diff_new_ins = new_ins - old_ins
        self._graph._emit_node_input_change(self, diff_old_ins, diff_new_ins)

    @property
    def output(self):
        return [self._graph.getVariable(v) for v in self._output]

    @output.setter
    def output(self, new_outs):
        new_outs = [self._graph.getVariable(v) if isinstance(
            v, str) else v for v in new_outs]
        old_outs = [self._graph.getVariable(v) for v in self._output]
        self._output = [v.name for v in new_outs]
        old_outs = set([v.name for v in old_outs])
        new_outs = set([v.name for v in new_outs])
        diff_old_outs = old_outs - new_outs
        diff_new_outs = new_outs - old_outs
        self._graph._emit_node_output_change(
            self, diff_old_outs, diff_new_outs)

    @property
    def attrs(self):
        return self._attrs

    def clearAttr(self):
        self._attrs.clear()

    def setAttr(self, key, val):
        if isinstance(val, np.ndarray):
            from .variable import Variable
            val = Variable(None, '', data=val)
        self._attrs[key] = val

    @property
    def prevNodes(self):
        return [n for v in self.input for n in v._src_nodes]

    @property
    def nextNodes(self):
        return [n for v in self.output for n in v._dst_nodes]

    @property
    def graph(self):
        return self._graph

    @graph.setter
    def graph(self, g):
        assert self._graph is None
        self._graph = g
        self._graph._emit_node_output_change(
            self, [], self._output)
        self._graph._emit_node_input_change(
            self, [], self._input)

    def removeFromGraph(self):
        self._graph._emit_node_output_change(
            self, self._output, [])
        self._graph._emit_node_input_change(
            self, self._input, [])
        self._graph._nodes.remove(self)
        self._graph = None

    def copyOut(self):
        new = copy.copy(self)
        new._graph = None
        return copy.deepcopy(new)
