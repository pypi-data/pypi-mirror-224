import networkx as nx
import matplotlib.pyplot as plt
from .SumNode import SumNode
from .MultNode import MultNode
from .SubsNode import SubsNode
from .DivNode import DivNode
from .ValueNode import ValueNode


class Graph:
    def __init__(self):
        self.graph = nx.DiGraph()

    def node(self, node):
        self.graph.add_node(node)

    def connect(self, node1, node2):
        self.graph.add_edge(node1, node2)

    def print_nodes(self):
        print(self.graph.nodes())

    def print_hello(self):
        print("Hello Autodiff")

    def draw_graph(self):
        pos = nx.circular_layout(self.graph)
        nx.draw(
            self.graph,
            pos,
            with_labels=True,
            node_size=500,
            node_color="skyblue",
            font_size=10,
            font_weight="bold",
            edge_color="gray",
        )

        plt.show()

    def forward(self):
        nodes = list(self.graph.nodes)
        return nodes[-1].result

    def backward(self):
        nodes = list(self.graph.nodes)
        nodes[-1].gradient = 1
        for node in reversed(nodes):
            if len(node.children) > 0:
                for children in node.children:
                    if isinstance(node, SumNode):
                        if isinstance(children, ValueNode):
                            pass
                        children.gradient = node.gradient * 1

                    if isinstance(node, SubsNode):
                        if children == node.children[0]:
                            if isinstance(children, ValueNode):
                                pass
                            else:
                                children.gradient = node.gradient * 1
                        if children == node.children[1]:
                            if isinstance(children, ValueNode):
                                pass
                            else:
                                children.gradient = node.gradient * -1

                    if isinstance(node, MultNode):
                        if children == node.children[0]:
                            if isinstance(children, ValueNode):
                                pass
                            else:
                                children.gradient = node.gradient * node.value2
                        if children == node.children[1]:
                            if isinstance(children, ValueNode):
                                pass
                            else:
                                children.gradient = node.gradient * node.value

                    if isinstance(node, DivNode):
                        if children == node.children[0]:
                            if isinstance(children, ValueNode):
                                pass
                            else:
                                children.gradient = node.gradient * (1 / node.value2)
                        if children == node.children[1]:
                            if isinstance(children, ValueNode):
                                pass
                            else:
                                children.gradient = node.gradient * (
                                    -(node.value / (node.value2) ** 2)
                                )
