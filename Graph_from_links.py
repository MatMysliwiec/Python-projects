import networkx as nx
import matplotlib.pyplot as plt


def create_graph(links):
    g = nx.Graph()
    g.add_edges_from(links)
    return g


def draw_graph(graph):
    pos = nx.circular_layout(graph)
    # pos = nx.kamada_kawai_layout(graph)
    # pos = nx.planar_layout(graph)
    # pos = nx.random_layout(graph)
    # pos = nx.shell_layout(graph)
    # pos = nx.spring_layout(graph)
    # pos = nx.spectral_layout(graph)
    # pos = nx.spiral_layout(graph)
    nx.draw(graph, pos, with_labels=True, font_weight='bold')
    plt.show()


if __name__ == "__main__":
    example_links = [
        ('A', 'B'),
        ('B', 'C'),
        ('C', 'A'),
        ('D', 'B'),
        ('D', 'C'),
        ('A', 'D')
    ]

    # Create graph
    my_graph = create_graph(example_links)

    # Draw the graph
    draw_graph(my_graph)
