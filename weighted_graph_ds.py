import networkx as nx

class WeightedGraph:
    def __init__(self):
        self.graph = nx.Graph()

    def add_node(self, node):
        self.graph.add_node(node)

    def add_edge(self, node1, node2, weight):
        self.graph.add_edge(node1, node2, weight=weight)

    def get_edge_weight(self, node1, node2):
        return self.graph[node1][node2]['weight']

    def find_shortest_path(self, source, target):
        return nx.shortest_path(self.graph, source, target, weight='weight')
