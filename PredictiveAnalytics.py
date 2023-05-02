import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

# Define the file path
file_path = "static/data/stop_times.csv"

# Load the file into a DataFrame
stop_times_df = pd.read_csv(file_path)

# Create a graph
Graph = nx.MultiDiGraph()

# Add edges with weights based on time difference
for i, row in stop_times_df.iterrows():
    if i < len(stop_times_df) - 1:
        current_stop_id = row['stop_id']
        next_stop_id = stop_times_df.loc[i+1, 'stop_id']
        current_time = pd.to_datetime(row['departure_time'])
        # Get the departure time of the next stop
        next_time = pd.to_datetime(stop_times_df.loc[i + 1, 'departure_time'])

        # Check if the hour is greater than 23
        if next_time.hour > 23:
            # If so, subtract 24 hours to wrap around to the next day
            next_time -= pd.Timedelta(hours=24)

        # Calculate the time difference between the current and next stops
        time_diff = next_time - current_time
        Graph.add_edge(current_stop_id, next_stop_id, weight=time_diff)

# Print the number of nodes and edges in the graph
print(f"Number of nodes: {Graph.number_of_nodes()}")
print(f"Number of edges: {Graph.number_of_edges()}")

# Find the shortest path from starting_stop_id to finishing_stop_id
starting_stop_id = '1231'
finishing_stop_id = '13'
shortest_path = nx.shortest_path(Graph, starting_stop_id, finishing_stop_id, weight='weight', method="dijkstra")

# Print the shortest path
print(shortest_path)

# Draw the graph
pos = nx.spring_layout(Graph)
nx.draw(Graph, pos, with_labels=True)
edge_labels = nx.get_edge_attributes(Graph, 'weight')
nx.draw_networkx_edge_labels(Graph, pos, edge_labels=edge_labels, font_size=8)
plt.show()