import networkx as nx


def dijkstra_with_networkx(graph, start):
    g = nx.DiGraph(graph)
    shortest_paths = nx.shortest_path_length(g, source=start, weight='weight', method='dijkstra')

    return shortest_paths


# Example usage:
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

start_node = 'A'
shortest_distances = dijkstra_with_networkx(graph, start_node)

print(f"Shortest distances from {start_node}: {shortest_distances}")
