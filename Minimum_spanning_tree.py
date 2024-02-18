import networkx as nx


def kruskal(graph):

    G = nx.Graph()

    for u, neighbors in graph.items():
        for v, weight in neighbors:
            G.add_edge(u, v, weight=weight)

    minimum_spanning_tree = nx.minimum_spanning_tree(G)

    return minimum_spanning_tree.edges(data=True)

# Example usage:
graph = {
    'A': [('B', 2), ('D', 5)],
    'B': [('A', 2), ('C', 1), ('D', 3)],
    'C': [('B', 1), ('D', 4)],
    'D': [('A', 5), ('B', 3), ('C', 4)]
}

minimum_spanning_tree = kruskal(graph)
print("Minimum Spanning Tree:", minimum_spanning_tree)
