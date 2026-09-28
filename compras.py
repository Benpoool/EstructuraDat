# Lista de compras organizada por categorías
compras = {
    "Frutas": {
        "Manzanas": 5,
        "Plátanos": 6,
        "Naranjas": 4
    },
    "Despensa": {
        "Arroz": 2,
        "Frijol": 3,
        "Pasta": 4
    },
    "Limpieza": {
        "Jabón": 3,
        "Cloro": 2
    }
}


def mostrar_compras(lista, nivel=0):
    for elemento, contenido in lista.items():

        print("  " * nivel + "- " + elemento)

        if isinstance(contenido, dict):
            mostrar_compras(contenido, nivel + 1)


print("=== LISTA DE COMPRAS ===")
mostrar_compras(compras)