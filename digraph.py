import pandas as pd
import networkx as nx
import numpy as np
import os

from plot_graphs import plot_absolute, plot_relational, save_graph
from haversine import haversine_distance, lat_lon_to_cartesian, cartesian_to_lat_lon, interpolate_points


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
                       traveled=row['distance'])
    return G


def calculate_haversine_for_edges(G):
    for origin, destination in G.edges():
        o_lat, o_lon = G.nodes[origin]['latitude'], G.nodes[origin]['longitude']
        d_lat, d_lon = G.nodes[destination]['latitude'], G.nodes[destination]['longitude']

        haversine = haversine_distance(o_lat, o_lon, d_lat, d_lon)
        G[origin][destination]['distance'] = haversine


def get_optimized_flights(G):
    optimized_flights = []

    for source, dest in G.edges():
        haversine = G[source][dest]['distance']
        traveled = G[source][dest]['traveled']

        if traveled > haversine:
            optimized_flights.append((source, dest, haversine, traveled))

    return optimized_flights


def get_flight_path(G, origin, destination, miles_apart: int = 10):
    o_lat, o_lon = G.nodes[origin]['latitude'], G.nodes[origin]['longitude']
    d_lat, d_lon = G.nodes[destination]['latitude'], G.nodes[destination]['longitude']

    total_distance = haversine_distance(o_lat, o_lon, d_lat, d_lon)
    num_points = int(total_distance / miles_apart)

    start = lat_lon_to_cartesian(o_lat, o_lon)
    end = lat_lon_to_cartesian(d_lat, d_lon)

    path_points = interpolate_points(start, end, num_points)
    return np.array([cartesian_to_lat_lon(x, y, z) for x, y, z in path_points])


def mean_excess_travel(flight_edges):
    excess_travels = [flight[3] - flight[2] for flight in flight_edges]
    return np.mean(excess_travels)


def median_excess_travel(flight_edges):
    excess_travels = [flight[3] - flight[2] for flight in flight_edges]
    return np.median(excess_travels)


def mean_percentage_excess_travel(flight_edges):
    percentage_excess_travels = [(flight[3] - flight[2]) / flight[2] * 100 for flight in flight_edges]
    return np.mean(percentage_excess_travels)


def median_percentage_excess_travel(flight_edges):
    percentage_excess_travels = [(flight[3] - flight[2]) / flight[2] * 100 for flight in flight_edges]
    return np.median(percentage_excess_travels)


def std_dev_excess_travel(flight_edges):
    excess_travels = [flight[3] - flight[2] for flight in flight_edges]
    return np.std(excess_travels)


def print_statistics(G, flight_edges):
    mean_excess = mean_excess_travel(flight_edges)
    median_excess = median_excess_travel(flight_edges)
    std_dev_excess = std_dev_excess_travel(flight_edges)
    mean_percentage_excess = mean_percentage_excess_travel(flight_edges)
    median_percentage_excess = median_percentage_excess_travel(flight_edges)

    print(len(flight_edges), "of", len(G.edges()), "optimized.")
    print("Mean Excess Travel:", mean_excess)
    print("Median Excess Travel:", median_excess)
    print("Standard Deviation of Excess Travel:", std_dev_excess)
    print("Mean Percentage Excess Travel:", mean_percentage_excess, "%")
    print("Median Percentage Excess Travel:", median_percentage_excess, "%")


def main():
    df_airlines, df_airports, df_flight_traffic = load_data()
    G = create_graph(df_airports, df_flight_traffic)
    calculate_haversine_for_edges(G)

    optimized_flights = get_optimized_flights(G)
    print_statistics(G, optimized_flights)

    # for source, destination, data in G.edges(data=True):
    #     print(get_flight_path(G, source, destination))


if __name__ == "__main__":
    main()
