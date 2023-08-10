from PySide6.QtWidgets import QGraphicsScene, QMenu, QGraphicsSceneContextMenuEvent, QDialog
from PySide6.QtCore import Signal, Slot
from ...ir import Graph, Node, Variable
from .normal_node import NormalGraphNode
from .io_node import IOGraphNode
from .edge import GraphEdge
from typing import List, Union
from grandalf.graphs import graph_core as GC
from grandalf.graphs import Graph as GG
from grandalf.graphs import Vertex as NN
from grandalf.graphs import Edge as EE
from grandalf.layouts import SugiyamaLayout
from ..ui import IOSummary, NodeSummary
import time


class GraphScene(QGraphicsScene):
    def __init__(self, ir: Graph, parent=None):
        super().__init__(parent)
        self._ir: Graph = ir
        self._normal_node = []
        self._io_node = []
        self._edge = []
        if self._ir is not None:
            # init var before node
            # because signal connect in node
            for v in self._ir.variables:
                self.bind_edge(v)
            for v in self._ir.input:
                self.bind_node(v)
            for v in self._ir.output:
                self.bind_node(v)
            for n in self._ir.nodes:
                self.bind_node(n)
        self.layout()

    def bind_node(self, ir: Union[Node, Variable]):
        if isinstance(ir, Node):
            n = NormalGraphNode(ir, self)
            self._normal_node.append(n)
        else:
            assert isinstance(ir, Variable)
            n = IOGraphNode(ir, self)
            self._io_node.append(n)
        assert ir.read_ext('bind_gnode') is None
        ir.set_ext('bind_gnode', n)
        self.addItem(n)
        n.connectToEdge()
        return n

    def bind_edge(self, ire: Variable):
        e = GraphEdge(ire, self)
        self._edge.append(e)
        assert ire.read_ext('bind_gedge') is None
        ire.set_ext('bind_gedge', e)
        self.addItem(e)
        return e

    def layout(self):
        ts = time.time()
        print('cvt to layout ir')
        N = {n.ir.id: NN(n) for n in self._normal_node}
        N.update({n.ir.id: NN(n) for n in self._io_node})
        if len(N) == 0:
            print('skip layout because empty graph')
            return
        E = []
        for n in N.values():
            n = n.data
            if isinstance(n, NormalGraphNode):
                src = n.ir.prevNodes
                dst = n.ir.nextNodes
                for v in n.ir.input:
                    if v.isInput:
                        src.append(v)
                for v in n.ir.output:
                    if v.isOutput:
                        dst.append(v)
            elif isinstance(n, IOGraphNode):
                src = n.ir.src
                dst = n.ir.dst
            else:
                raise RuntimeError(f'Unexcept type: {type(n)}')
            for s in src:
                E.append(
                    EE(N[s.id], N[n.ir.id], data=f'{s.name} -> {n.ir.name}'))
            for d in dst:
                E.append(
                    EE(N[n.ir.id], N[d.id], data=f'{n.ir.name} -> {d.name}'))
        g = GG(list(N.values()), E)
        print('cvt done:', time.time() - ts, 's')
        print('graph_core num:', len(g.C))
        ts = time.time()
        print('layout start')
        for n in N.values():
            rect = n.data.boundingRect()
            assert rect is not None

            class HWView(object):
                w, h = rect.width(), rect.height()
            n.view = HWView()
            # print(n.data.ir.name, n.view.w, n.view.h)
        sug = SugiyamaLayout(g.C[0])
        sug.init_all()
        sug.draw()
        for n in g.C[0].sV:
            x, y = n.view.xy
            w = n.view.w
            h = n.view.h
            x = x - w / 2
            y = y - h / 2
            # print(n.data.ir.name, x, y)
            n.data.setPos(x, y)
            # print(n.data.ir.name, n.data.pos())
        print('layout done:', time.time() - ts, 's')

    def contextMenuEvent(self, event: QGraphicsSceneContextMenuEvent) -> None:
        super().contextMenuEvent(event)

        def add_node():
            n = self.addNode()
            n.setPos(event.scenePos())

        def add_i(input):
            def f():
                n = self.addIO(input)
                n.setPos(event.scenePos())
            return f
        m = QMenu()
        new_node_act = m.addAction("New Node")
        new_node_act.triggered.connect(add_node)
        new_input_act = m.addAction("New Input")
        new_input_act.triggered.connect(add_i(True))
        new_output_act = m.addAction("New Output")
        new_output_act.triggered.connect(add_i(False))
        m.exec(event.screenPos())
        event.accept()

    def addNode(self):
        dialog = NodeSummary()
        dialog.setWindowTitle('Add Node')
        ret = dialog.exec()
        if ret == QDialog.DialogCode.Accepted:
            ret = dialog.getRet()
            n = self._ir.addNode(ret['name'], ret['op_type'])
            n.input = ret['inputs']
            n.output = ret['output']
            n.clearAttr()
            for k, v in ret['attrs'].items():
                n.setAttr(k, v)
            return self.bind_node(n)
        return None

    def addIO(self, input=True):
        dialog_name = 'Input' if self._ir.isInput else 'Output'
        dialog = IOSummary()
        dialog.setWindowTitle('Add ' + dialog_name)
        ret = dialog.exec()
        if ret == QDialog.DialogCode.Accepted:
            ret = dialog.getRet()
            v = self._ir.getVariable(ret['name'])
            v.shape = ret['shape']
            v.type = ret['type']
            if input:
                self._ir.markInput(v)
            else:
                self._ir.markOutput(v)
            self.bind_edge(v)
            return self.bind_node(v)
        return None
