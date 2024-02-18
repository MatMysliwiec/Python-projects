import networkx as nx
import matplotlib.pyplot as plt


def find_eulerian_path_or_cycle(graph):
    if nx.is_connected(graph):
        odd_degree_nodes = [node for node in graph.nodes() if graph.degree(node) % 2 != 0]

        if len(odd_degree_nodes) == 0:
            return "Eulerian cycle"
        elif len(odd_degree_nodes) == 2:
            return "Eulerian path"
        else:
            return "Not possible"
    else:
        return "Not possible"


def visualize_graph(graph):
    pos = nx.spring_layout(graph)
    nx.draw(graph, pos, with_labels=True, font_weight='bold')
    plt.show()


example_links = [(1, 0), (0, 2), (2, 1), (0, 3), (3, 4)]
G = nx.Graph()
G.add_edges_from(example_links)

result = find_eulerian_path_or_cycle(G)
print(f"Eulerian Path/Cycle: {result}")

if result in ["Eulerian path", "Eulerian cycle"]:
    visualize_graph(G)
