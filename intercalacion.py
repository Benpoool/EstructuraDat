"""
Problema: dos grupos (A y B) entregan sus calificaciones YA ORDENADAS de
menor a mayor. Se necesita una lista general ordenada con ambos grupos.
"""


def intercalar(lista_a, lista_b):
    resultado = []
    i = 0  # índice sobre lista_a
    j = 0  # índice sobre lista_b

    # Mientras ambas listas tengan elementos por comparar
    while i < len(lista_a) and j < len(lista_b):
        if lista_a[i] <= lista_b[j]:
            resultado.append(lista_a[i])
            i += 1
        else:
            resultado.append(lista_b[j])
            j += 1
        print(f"  Comparando -> resultado parcial: {resultado}")

    # Copiar lo que sobre de la lista que aún tenga elementos
    while i < len(lista_a):
        resultado.append(lista_a[i])
        i += 1
    while j < len(lista_b):
        resultado.append(lista_b[j])
        j += 1

    return resultado


def main():
    grupo_a = [55, 60, 70, 82, 90, 100]
    grupo_b = [48, 65, 75, 88]

    print("=== INTERCALACIÓN DE CALIFICACIONES ===")
    print("Grupo A (ordenado):", grupo_a)
    print("Grupo B (ordenado):", grupo_b)
    print("\nProceso:")

    lista_general = intercalar(grupo_a, grupo_b)

    print("\nLista general ordenada:", lista_general)
    print("Total de alumnos:", len(lista_general))


if __name__ == "__main__":
    main()
