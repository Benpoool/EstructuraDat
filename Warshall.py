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

nodos = list(G.nodes())
n = len(nodos)

alcanzabilidad = [[0] * n for _ in range(n)]

for i in range(n):
    alcanzabilidad[i][i] = 1

for a, b in G.edges():
    i = nodos.index(a)
    j = nodos.index(b)

    alcanzabilidad[i][j] = 1
    alcanzabilidad[j][i] = 1

for k in range(n):
    for i in range(n):
        for j in range(n):
            alcanzabilidad[i][j] = (
                alcanzabilidad[i][j] or
                (alcanzabilidad[i][k] and alcanzabilidad[k][j])
            )

print("ALGORITMO DE WARSHALL")
print("----------------------")

print("    ", end="")
for nodo in nodos:
    print(f"{nodo:>4}", end="")
print()

for i in range(n):
    print(f"{nodos[i]:>4}", end="")

    for j in range(n):
        print(f"{int(alcanzabilidad[i][j]):>4}", end="")

    print()