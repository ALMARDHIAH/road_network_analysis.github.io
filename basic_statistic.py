import osmnx as ox
import matplotlib.pyplot as plt

# Downloading geospatial data from OSM
graf = ox.graph_from_place(
“putrajaya”,
network_type='drive',
simplify=True)

# Mengunjurkan graf berdasarkan UTM
graf_proj=ox.project_graph(graf)

# Mendapatkan statistik deskriptif rangkaian
ox.basic_stats(graf_proj)
