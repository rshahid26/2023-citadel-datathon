import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd

df_airlines = pd.read_csv("./datasets/airlines.csv")
df_airports = pd.read_csv("./datasets/airports.csv", encoding='ISO-8859-1')
df_flight_traffic = pd.read_csv("./datasets/flight_traffic.csv")


G = nx.MultiDiGraph()

for airport in df_airports['airport_id']:
    G.add_node(airport)


def add_edge(row):
    G.add_edge(row['origin_airport'], row['destination_airport'],
               airline=row['airline_id'],
               distance=row['distance'])


df_flight_traffic.head(1000).apply(add_edge, axis=1)

print(G.nodes())
print(G.edges())

# print(nx.shortest_path(G, "A", "D", weight="weight"))
#
# T = nx.bfs_tree(G, source='A')
# print("Nodes in DFS order:", list(T.nodes))

# PLOT DIGRAPH
# nx.draw(G, with_labels=True)
# plt.show()