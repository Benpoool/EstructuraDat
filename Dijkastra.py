import networkx as nx

G = nx.Graph()

conexiones = [
    ("A", "B", 4),
    ("A", "C", 2),
    ("B", "C", 1),
    ("B", "D", 5),
    ("C", "D", 8),
    ("C", "E", 10),
    ("D", "E", 2)
]

G.add_weighted_edges_from(conexiones)

inicio = "A"

distancias = nx.single_source_dijkstra_path_length(
    G, inicio, weight="weight"
)

rutas = nx.single_source_dijkstra_path(
    G, inicio, weight="weight"
)

print("ALGORITMO DE DIJKSTRA")
print("----------------------")

for nodo in G.nodes():
    print(f"Destino: {nodo}")
    print(f"Distancia: {distancias[nodo]}")
    print(f"Ruta: {' -> '.join(rutas[nodo])}")
    print()