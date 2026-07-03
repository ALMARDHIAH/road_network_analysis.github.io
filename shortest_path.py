import osmnx as ox
import matplotlib.pyplot as plt
import numpy as np
import networkx as nx
from matplotlib.patches import FancyArrowPatch

# Memuat turun data georuang daripada OSM
graf = ox.graph_from_place("putrajaya",
   network_type='drive',
   simplify=True)

# Mengunjurkan graf berdasarkan UTM
graf_proj=ox.project_graph(graf)

# Memuat turun GeoDataFrame bucu dan tepi rangkaian
bucu, tepi= ox.graph_to_gdfs(graf_proj)

#========================================================

# Mendapatkan pemusatan kedekatan (dji)
pemusatan_kedekatan_dji=nx.closeness_centrality(
graf_proj,
distance='length')

# Mendapatkan bucu dengan nilai kedekatan dji tertinggi
bucu_kedekatan_tertinggi=max(pemusatan_kedekatan_dji,
key=pemusatan_kedekatan_dji.get)
nilai_kedekatan_tertinggi=max(pemusatan_kedekatan_dji.values())
print("bucu tertinggi", bucu_kedekatan_tertinggi,
 "dengan nilainya", nilai_kedekatan_tertinggi)

#========================================================

# Mendapatkan pemusatan pengantaraan
pemusatan_pengantaraan=nx.betweenness_centrality(
graf_proj,
weight='length',
normalized=True)

# Mendapatkan bucu dengan nilai pengantaraan tertinggi
bucu_pengantaraan_tertinggi=max(pemusatan_pengantaraan,
key=pemusatan_pengantaraan.get)
nilai_pengantaraan_tertinggi=max(pemusatan_pengantaraan.values())
print("bucu tertinggi", bucu_pengantaraan_tertinggi,
 "dengan nilainya", nilai_pengantaraan_tertinggi)

#========================================================

# route2 sebagai lintasan terpendek dari 
# bucu dengan nilai pengantaraan tertinggi 
# menuju bucu dengan nilai kedekatan tertinggi
route2=list(ox.k_shortest_paths(
    graf_proj,
    orig = bucu_pengantaraan_tertinggi , 
    dest = bucu_kedekatan_tertinggi , 
    k = 1 ,
    weight = 'length' ))
print(route2)

#========================================================

warna_nod = {
    bucu_kedekatan_tertinggi: 'red',
    bucu_pengantaraan_tertinggi: 'red',
   }
saiz_nod = {
    bucu_kedekatan_tertinggi: 5,
    bucu_pengantaraan_tertinggi: 5,
}

#========================================================
# Memplot lintasan terpendek
fig, ax = ox.plot_graph_route(
    graf_proj,
    route2[0],
    route_color='blue',
    route_linewidth=0.3,
    figsize=(8, 8.5),
node_size=[saiz_nod.get(n, 1) for n in
graf_proj.nodes],
node_color=[warna_nod.get(n, 'grey') for n in
 graf_proj.nodes],
    node_zorder=3,
    node_alpha=0.5,
    edge_linewidth=0.2,
    bgcolor='white',
    save=False,
    show=False,
    close=False
)

# Melukis arah lintasan
for i in range(len(route2[0]) - 1):
    start_node = route2[0][i]
    end_node = route2[0][i + 1]
start_coords = graf_proj.nodes[start_node]['x'],
    graf_proj.nodes[start_node]['y']
end_coords = graf_proj.nodes[end_node]['x'],
  graf_proj.nodes[end_node]['y']
arrow = FancyArrowPatch(start_coords,
   end_coords,
   color='red',
   arrowstyle='->',
   mutation_scale=5,
   lw=0.3,
   alpha=0.7)
    ax.add_patch(arrow)

plt.show() 
 
