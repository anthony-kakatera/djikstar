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

    def shortest_path_between(self, source, target):
        shortest_path = self.weighted_graph.find_shortest_path(source, target)

        if shortest_path:
            path_cost = 0
            for i in range(len(shortest_path) - 1):
                path_cost += self.weighted_graph.get_edge_weight(shortest_path[i], shortest_path[i + 1])
            shortest_path_str = f"{shortest_path}, {path_cost}"
            return shortest_path_str

        return "No path found."

    # Calculating the shortest path
    # def calculate_shortest_path(self, source, target):
    #     shortest_path = self.weighted_graph.find_shortest_path(source, target)
    #     if shortest_path:
    #         shortest_distance = sum(
    #             self.weighted_graph.get_edge_weight(shortest_path[i], shortest_path[i + 1])
    #             for i in range(len(shortest_path) - 1)
    #         )
    #         return shortest_path, shortest_distance
    #     else:
    #         return [], float('inf')
    
    # # districts print out   
    # def nodes_in_shortest_path(self, source, target):
    #     shortest_path, _ = self.calculate_shortest_path(source, target)
    #     return shortest_path
        
# Running the code
if __name__ == '__main__':
    districts_instance = Districts()
    districts_instance.use_weighted_graph()

    # Finding the shortest path
    shortest_path = districts_instance.shortest_path_between('Dedza', 'Nkhotakota')

    if shortest_path:
        print("Shortest path from Dedza to Nkhotakota:", shortest_path)
    else:
        print("No path from Dedza to Nkhotakota.")
