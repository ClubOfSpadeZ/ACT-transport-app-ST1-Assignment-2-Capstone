# read csv file
# build a network with no duplicate edges going to and from the same 2 vertex (stop)
# build new spanning tree
# get times

import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
from datetime import datetime

# Define the file path
file_path = "static/data/stop_times.csv"

# Define the chunk size
chunksize = 10000

# Create a graph
graph = nx.MultiDiGraph()

# Add edges with weights based on time difference
stop_times_df = pd.read_csv(file_path)
trips_df = pd.read_csv('static/data/trips.csv')
routes_df = pd.DataFrame({'route_id': []})

i = 0
flag = False
for index, row in stop_times_df.iterrows():
    if flag:
        if row['stop_sequence'] == 1:
            flag = False
        continue
    current_stop = row['stop_id']
    if current_stop in graph:
        graph.add_node(current_stop)
    if row['stop_sequence'] == 1:
        matching_trips = trips_df.loc[trips_df['trip_id'] == stop_times_df.loc[index, 'trip_id']]
        # print(matching_trips)
        if not matching_trips.empty:
            matching_index = matching_trips.index[0]
            # print(matching_index)
            print(matching_trips['route_id'])
            print(routes_df.loc[:, 'route_id'])
            if routes_df.loc[:, 'route_id'] == matching_trips['route_id']:
                flag = True
                print('skip')
            else:
                routes_df = routes_df.add(matching_trips)
        continue
    else:
        previous_stop = stop_times_df.loc[index - 1, 'stop_id']
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
def graphNetwrok(StopFrom, StopTo, StartTime):
    pass
def outputVaules():
    # Print the number of nodes and edges in the graph
    print(f"Number of nodes: {graph.number_of_nodes()}")
    print(f"Number of edges: {graph.number_of_edges()}")

if __name__ == '__main__':
    time_str = '00:39:00'
    elapsed_seconds = (datetime.strptime(time_str, '%H:%M:%S').minute * 60) + (datetime.strptime(time_str, '%H:%M:%S').hour * 3600)

    print(elapsed_seconds)
    outputVaules()
