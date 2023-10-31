class WeightedGraph:
    def __init__(self):
        self.graph = {}

    def add_node(self, node):
        if node not in self.graph:
            self.graph[node] = {}

    def add_edge(self, node1, node2, weight):
        self.add_node(node1)
        self.add_node(node2)

        self.graph[node1][node2] = weight
        self.graph[node2][node1] = weight

    def get_edge_weight(self, node1, node2):
        if node1 in self.graph and node2 in self.graph:
            return self.graph[node1].get(node2, float('inf'))
        return float('inf')

    def find_shortest_path(self, source, target):
        if source not in self.graph or target not in self.graph:
            return None

        distances = {node: float('inf') for node in self.graph}
        distances[source] = 0
        visited = set()

        while True:
            # Unvisited node with the smallest distance
            current_node = min((node for node in distances if node not in visited), key=distances.get, default=None)
            if current_node is None:
                break  # None left to explore
            visited.add(current_node)

            for neighbor, weight in self.graph[current_node].items():
                if neighbor not in visited:
                    new_distance = distances[current_node] + (weight or float('inf'))
                    if new_distance < distances[neighbor]:
                        distances[neighbor] = new_distance

        if distances[target] == float('inf'):
            return None  # Unreachable

        path = [target]
        while target != source:
            neighbors = self.graph.get(target, {})
            best_neighbor = min(neighbors, key=distances.get)
            path.insert(0, best_neighbor)
            target = best_neighbor

        return path
