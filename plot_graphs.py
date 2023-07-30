import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors


def normalize_distances(G):
    distances = [d['distance'] for _, _, d in G.edges(data=True)]
    min_distance = min(distances)
    max_distance = max(distances)

    norm_distances = [(d - min_distance) / (max_distance - min_distance) for d in distances]
    return norm_distances


def plot_relational(G):
    norm_distances = normalize_distances(G)

    cmap = plt.get_cmap('YlOrRd')
    edge_colors = [cmap(d) for d in norm_distances]

    nx.draw(G, with_labels=True, edge_color=edge_colors)
    plt.show()


def plot_absolute(G, df_airports):

    positions = {airport: (row['longitude'], row['latitude'])
                 for airport, row in df_airports.set_index('airport_id').iterrows()}

    nx.draw(G, positions, with_labels=True)
    plt.show()


def save_graph(G, df_airports, title=None):

    positions = {airport: (row['longitude'], row['latitude'])
                 for airport, row in df_airports.set_index('airport_id').iterrows()}

    norm_distances = normalize_distances(G)
    cmap = plt.get_cmap('YlOrRd')
    edge_colors = [cmap(d) for d in norm_distances]

    plt.figure(figsize=(10, 6))
    nx.draw(G, positions, with_labels=True, edge_color=edge_colors)

    if title:
        plt.title(title)
    plt.savefig(f"./assets/{title or 'graph'}.png")

    plt.show()
