from weighted_graph_ds import WeightedGraph

class Districts:
    def __init__(self):
        # Instance of WeightedGraph
        self.weighted_graph = WeightedGraph()

    def use_weighted_graph(self):
        # Nodes
        self.weighted_graph.add_node('Mchinji')
        self.weighted_graph.add_node('Kasungu')
        self.weighted_graph.add_node('Lilongwe')
        self.weighted_graph.add_node('Dowa')
        self.weighted_graph.add_node('Ntchisi')
        self.weighted_graph.add_node('Dedza')
        self.weighted_graph.add_node('Salima')
        self.weighted_graph.add_node('Nkhotakota')
        self.weighted_graph.add_node('Ntcheu')
        # Weighted edges
        self.weighted_graph.add_edge('Mchinji', 'Kasungu', 141)
        self.weighted_graph.add_edge('Mchinji', 'Lilongwe', 109)
        self.weighted_graph.add_edge('Kasungu', 'Dowa', 117)
        self.weighted_graph.add_edge('Kasungu', 'Ntchisi', 66)
        self.weighted_graph.add_edge('Lilongwe', 'Dowa', 55)
        self.weighted_graph.add_edge('Lilongwe', 'Dedza', 92)
        self.weighted_graph.add_edge('Dowa', 'Ntchisi', 38)
        self.weighted_graph.add_edge('Dowa', 'Salima', 67)
        self.weighted_graph.add_edge('Ntchisi', 'Nkhotakota', 66)
        self.weighted_graph.add_edge('Nkhotakota', 'Salima', 112)
        self.weighted_graph.add_edge('Salima', 'Dedza', 96)
        self.weighted_graph.add_edge('Dedza', 'Ntcheu', 74)
