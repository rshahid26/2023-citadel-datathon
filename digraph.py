import pandas as pd
import networkx as nx
import os

from plot_graphs import plot_absolute, plot_relational, save_graph


def load_data():
    df_airlines = pd.read_csv("./datasets/airlines.csv")
    df_airports = pd.read_csv("./datasets/airports.csv", encoding='ISO-8859-1')
    df_flight_traffic = pd.read_csv("./datasets/unique_flights.csv")
    return df_airlines, df_airports, df_flight_traffic


def create_graph(df_airports, df_flight_traffic):
    G = nx.DiGraph()

    for index, row in df_airports.iterrows():
        G.add_node(row['airport_id'], longitude=row['longitude'], latitude=row['latitude'])

    for index, row in df_flight_traffic.iterrows():
        origin = row['origin_airport']
        destination = row['destination_airport']

        if origin in G and destination in G:
            G.add_edge(origin, destination,
                       airline=row['airline_id'],
                       distance=row['distance'])
    return G


def main():
    df_airlines, df_airports, df_flight_traffic = load_data()
    G = create_graph(df_airports, df_flight_traffic)

    print(G.nodes())
    print(G.edges())

    plot_relational(G)


if __name__ == "__main__":
    main()
