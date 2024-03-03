import networkx as nx
import matplotlib.pyplot as plt


def create_graph(links):
    g = nx.Graph()
    g.add_edges_from(links)
    return g


def is_connected(graph):
    statement = nx.is_connected(graph)
    if statement:
        return print("The graph is connected")
    else:
        return print("The graph is not connected")


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

    my_graph = create_graph(example_links)

    is_connected(my_graph)

    draw_graph(my_graph)
