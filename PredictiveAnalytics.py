# read csv file
# build a network with no duplicate edges going to and from the same 2 vertex (stop)
# build new spanning tree
# get times

import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
from datetime import datetime
from geopy.distance import geodesic
import ast
from typing_extensions import Literal

# Define the file path
file_path = "static/data/stop_times.csv"

def makeGraph():
    # Create a graph
    graph = nx.MultiDiGraph()

    # Add nodes to the graph
    for index, row in stops_df.iterrows():
        stop_id = row['stop_id']
        stop_name = row['stop_name']
        stop_lat = row['stop_lat']
        stop_lon = row['stop_lon']
        pos = f"{stop_lon},{stop_lat}"
        graph.add_node(stop_id, name=stop_name, pos=pos)
        print(f"Number of nodes: {graph.number_of_nodes()}")

    # Add edges to the graph
    for i in range(len(stops_df)):
        stop1 = stops_df.iloc[i]
        print(stop1['stop_id'])
        for j in range(i + 1, len(stops_df)):
            stop2 = stops_df.iloc[j]
            distance = geodesic((stop1['stop_lat'], stop1['stop_lon']), (stop2['stop_lat'], stop2['stop_lon'])).m
            if distance <= 200:
                graph.add_edge(stop1['stop_id'], stop2['stop_id'], weight=distance)

    i = 0
    flag = False
    for index, row in stop_times_df.iterrows():
        # print(trips_df.loc[trips_df['trip_id'] == row['trip_id']].iloc[0]['route_id'])
        # Checks if we are at begin of route agian, if so then resume normal code
        if flag:
            if trips_df.loc[trips_df['trip_id'] == row['trip_id']].iloc[0]['route_id'] not in routes_df['route_id'].values:
                flag = False
            else:
                continue

        # Sets flag True if the same route_id is added at the point where drop_off_type = 1
        if trips_df.loc[trips_df['trip_id'] == row['trip_id']].iloc[0]['route_id'] in routes_df['route_id'].values and row['stop_sequence'] == 1:
            flag = True
        else:
            matching_trips = trips_df.loc[trips_df['trip_id'] == stop_times_df.loc[index, 'trip_id']]
            if matching_trips.iloc[0]['route_id'] not in unique_route_ids:
                routes_df = pd.concat([matching_trips, routes_df])
                unique_route_ids.add(matching_trips.iloc[0]['route_id'])
                print(routes_df)
                print(f"Number of nodes: {graph.number_of_nodes()}")
                print(f"Number of edges: {graph.number_of_edges()}")

        current_stop = row['stop_id']

        # Checks if we are at begin of route
        if row['stop_sequence'] == 1:
            continue
        else:
            previous_stop = stop_times_df.loc[index - 1, 'stop_id']
            # Make an edge if previous_stop and current_stop are not in the graph with the same trip_id
            try:
                current_time = pd.to_datetime(row['arrival_time'])
            except:
                hour, minute, second = map(int, row['arrival_time'].split(':'))
                hour0 = 0
                current_time = pd.to_datetime(f"{hour0:02d}:{minute:02d}:{second:02d}")
            try:
                previous_time = pd.to_datetime(stop_times_df.loc[index - 1, 'arrival_time'])
            except:
                hour, minute, second = map(int, row['arrival_time'].split(':'))
                hour0 = 0
                previous_time = pd.to_datetime(f"{hour0:02d}:{minute:02d}:{second:02d}")
            time_diff = (current_time - previous_time).total_seconds() // 60
            graph.add_edge(previous_stop, current_stop, weight=time_diff)
            print(time_diff)

def graphNetwrok(StopFrom: str, StopTo: str, show: Literal['Path', 'Graph'] = 'Graph'):
    print(f"Number of nodes: {graph.number_of_nodes()}")
    print(f"Number of edges: {graph.number_of_edges()}")

    # Make all edge weights positive
    min_weight = min(graph.edges(data='weight'), key=lambda x: x[2])[2]
    if min_weight < 0:
        offset = abs(min_weight) + 1
        for u, v, data in graph.edges(data=True):
            data['weight'] += offset

    path = nx.dijkstra_path(graph, starting_stop, destination_stop, weight='weight')

    print(path)

    # Create subgraph of graph that contains only the nodes and edges in the path
    subgraph = nx.Graph()
    subgraph.add_nodes_from(path)
    subgraph_edges = [(path[i], path[i + 1]) for i in range(len(path) - 1)]
    subgraph.add_edges_from(subgraph_edges)

    # Extract node positions from graph
    pos = nx.get_node_attributes(graph, "pos")

    # Convert position strings to tuples
    for key, value in pos.items():
        pos[key] = ast.literal_eval(value)

    # Check for nodes with missing positions
    missing_pos = [n for n in graph.nodes() if n not in pos]
    if missing_pos:
        print(f"The following nodes do not have positions: {missing_pos}")
    else:
        if show == 'Path':
            # Draw the path
            fig, ax = plt.subplots(figsize=(12, 8))
            nx.draw(subgraph, pos, with_labels=True, node_color='lightblue', edge_color='gray', ax=ax)
            plt.show()
        else:
            # Draw the graph
            fig, ax = plt.subplots(figsize=(12, 8))
            nx.draw(graph, pos, with_labels=True, node_color='lightblue', edge_color='gray', ax=ax)
            plt.show()

if __name__ == '__main__':
    stop_times_df = pd.read_csv(file_path)
    trips_df = pd.read_csv('static/data/trips.csv')
    routes_df = pd.DataFrame({'route_id': []})
    matching_trips = pd.DataFrame()
    unique_route_ids = set(routes_df['route_id'].tolist())
    stops_df = pd.read_csv('static/data/stops.csv')

    # Load graph from GraphML file
    graph = nx.read_graphml("my_graph.graphml")

    starting_stop = '1231'
    destination_stop = '4529'

    graphNetwrok(starting_stop, destination_stop, show='Graph')
