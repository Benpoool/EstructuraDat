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

arbol = nx.minimum_spanning_tree(
    G,
    algorithm="kruskal",
    weight="weight"
)

print("ALGORITMO DE KRUSKAL")
print("---------------------")

costo_total = 0

for origen, destino, datos in arbol.edges(data=True):
    costo = datos["weight"]

    print(f"{origen} -- {destino}: {costo}")

    costo_total += costo

print("\nCosto total del arbol:", costo_total)