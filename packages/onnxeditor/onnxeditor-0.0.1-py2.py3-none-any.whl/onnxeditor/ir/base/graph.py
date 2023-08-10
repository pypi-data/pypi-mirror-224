from typing import TYPE_CHECKING, List, Dict, Union, Set
from collections import deque
from .obj import IRObj

if TYPE_CHECKING:
    from .node import Node
    from .variable import Variable


class Graph(IRObj):
    def __init__(self) -> None:
        super().__init__()

        self._variables: Dict['Variable'] = {}

        self.name: str = None
        self.doc_string: str = None
        self._nodes: List['Node'] = []
        self._input: List[str] = []
        self._output: List[str] = []

        self.displayAttr('name')
        self.displayAttr('doc_string')
        self.displayAttr('_input', name='input')
        self.displayAttr('_output', name='output')
        self.displayAttr('nodes')
        self.displayAttr('variables')

    def autoMarkInput(self):
        self._input.extend(
            [k for k, v in self._variables.items() if v.canBeInput])

    def markInput(self, v: Union[str, 'Variable']):
        if not isinstance(v, str):
            v = v.name
        self.getVariable(v)
        self._input.append(v)

    def unMarkInput(self, v):
        self._input.remove(v)

    def markOutput(self, v: Union[str, 'Variable']):
        if not isinstance(v, str):
            v = v.name
        self.getVariable(v)
        self._output.append(v)

    def unMarkOutput(self, v):
        self._output.remove(v)

    @property
    def nodes(self):
        return [n for n in self._nodes]

    @property
    def variables(self):
        return tuple(self._variables.values())

    @property
    def input(self):
        return [v for v in self._variables.values() if v.name in self._input]

    @property
    def output(self):
        return [v for v in self._variables.values() if v.name in self._output]

    def addNode(self, node: str, op_type: str) -> 'Node':
        from .node import Node
        if isinstance(node, str):
            node = Node(self, node, op_type)
            self._nodes.append(node)
        else:
            assert isinstance(node, Node)
            node.graph = self
            self._nodes.append(node)
        return node

    def delNode(self, node: 'Node'):
        if node in self._nodes:
            node.removeFromGraph()

    def addVariable(self, v: Union[str, 'Variable']) -> 'Variable':
        from .variable import Variable
        if isinstance(v, str):
            v = Variable(self, v)
        assert isinstance(v, Variable)
        assert v.name not in self._variables
        self._variables[v.name] = v
        return v

    def getVariable(self, name: str, auto_create=True) -> 'Variable':
        if auto_create and name not in self._variables:
            return self.addVariable(name)
        else:
            assert name in self._variables, name
            return self._variables[name]

    def hasVariable(self, v: 'Variable') -> bool:
        if v.name not in self._variables:
            return False
        return self._variables[v.name] == v

    def delVariable(self, v: 'Variable'):
        if isinstance(v, str):
            name = v
        else:
            name = v.name
        if name in self._variables and v is self._variables.get(name):
            v = self.getVariable(v)
            v.removeFromGraph()

    def topoSort(self):
        visited = {}
        nbinputs = {}
        wklist = deque()
        for n in self.getField('nodes').val:
            visited[n] = False
            nbinputs[n] = len(n.prevNodes)
            if nbinputs[n] == 0:
                wklist.append(n)

        sorted = []
        for _ in range(len(visited)):
            if len(wklist) == 0:
                break
            n = wklist.popleft()
            for next_n in n.nextNode:
                nbinputs[next_n] -= 1
                if nbinputs[next_n] == 0:
                    wklist.append(next_n)
            visited[n] = True
            sorted.append(n)
        if all(visited.values()):
            self.getField('nodes').val = sorted
        else:
            raise RuntimeError(
                f'TopoSort error: {[n for n in visited if visited[n] == False]}')

    def _emit_node_input_change(self, node: 'Node', old_ins: Set[str], new_ins: Set[str]):
        for i in old_ins:
            v = self.getVariable(i, False)
            v._dst_nodes.remove(node)
        for i in new_ins:
            v = self.getVariable(i)
            v._dst_nodes.add(node)

    def _emit_node_output_change(self, node: 'Node', old_outs: Set[str], new_outs: Set[str]):
        for i in old_outs:
            v = self.getVariable(i, False)
            v._src_nodes.remove(node)
        for i in new_outs:
            v = self.getVariable(i)
            v._src_nodes.add(node)
