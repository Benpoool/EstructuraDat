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

distancias = dict(
    nx.floyd_warshall(G, weight="weight")
)

print("ALGORITMO DE FLOYD")
print("-------------------")

nodos = list(G.nodes())

print("    ", end="")
for nodo in nodos:
    print(f"{nodo:>6}", end="")
print()

for origen in nodos:
    print(f"{origen:>4}", end="")

    for destino in nodos:
        distancia = distancias[origen][destino]

        if distancia == float("inf"):
            print(f"{'INF':>6}", end="")
        else:
            print(f"{distancia:>6}", end="")

    print()