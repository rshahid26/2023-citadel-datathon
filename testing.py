import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd

df_airlines = pd.read_csv("./datasets/airlines.csv")
df_airports = pd.read_csv("./datasets/airports.csv", encoding='ISO-8859-1')
df_flight_traffic = pd.read_csv("./datasets/unique_flights.csv")

G = nx.MultiDiGraph()

for index, row in df_airports.iterrows():
    G.add_node(row['airport_id'], longitude=row['longitude'], latitude=row['latitude'])


for index, row in df_flight_traffic.iterrows():
    origin = row['origin_airport']
    destination = row['destination_airport']

    if origin in G and destination in G:
        G.add_edge(origin, destination,
                   airline=row['airline_id'],
                   distance=row['distance'])


print(G.nodes())
print(G.edges())


positions = {airport: (row['longitude'], row['latitude'])
             for airport, row in df_airports.set_index('airport_id').iterrows()}

nx.draw(G, positions, with_labels=True)
# nx.draw(G, with_labels=True)
plt.show()

