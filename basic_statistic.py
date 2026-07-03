import osmnx as ox
import matplotlib.pyplot as plt

# Downloading geospatial data from OSM
graf = ox.graph_from_place(
“putrajaya”,
network_type='drive',
simplify=True)

# Projecting the graph based on UTM
graf_proj=ox.project_graph(graf)

# Getting the descriptive statistics of the network
ox.basic_stats(graf_proj)
