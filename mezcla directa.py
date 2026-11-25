"""
Problema: ordenar un archivo de folios de productos (uno por línea) usando
archivos auxiliares, como en un ordenamiento externo. En cada pasada se
distribuyen bloques de tamaño fijo (1, 2, 4, 8...) en dos archivos auxiliares
y luego se mezclan de regreso al archivo principal.
"""
import os

ARCHIVO = "folios.txt"
AUX1 = "aux1.txt"
AUX2 = "aux2.txt"


def siguiente(archivo):
    linea = archivo.readline()
    return int(linea) if linea.strip() else None


def leer_todo(ruta):
    with open(ruta) as f:
        return [int(x) for x in f.read().split()]


def distribuir(origen, aux1, aux2, tam):
    total = 0
    with open(origen) as f, open(aux1, "w") as a1, open(aux2, "w") as a2:
        destino = a1
        contador = 0
        for linea in f:
            destino.write(linea)
            total += 1
            contador += 1
            if contador == tam:
                contador = 0
                destino = a2 if destino is a1 else a1
    return total


def mezclar(aux1, aux2, destino, tam):
    with open(aux1) as f1, open(aux2) as f2, open(destino, "w") as out:
        x = siguiente(f1)
        y = siguiente(f2)
        while x is not None or y is not None:
            c1 = 0  # elementos tomados del bloque actual de aux1
            c2 = 0  # elementos tomados del bloque actual de aux2
            while (c1 < tam and x is not None) or (c2 < tam and y is not None):
                toma_x = (c1 < tam and x is not None) and (
                    c2 >= tam or y is None or x <= y
                )
                if toma_x:
                    out.write(f"{x}\n")
                    x = siguiente(f1)
                    c1 += 1
                else:
                    out.write(f"{y}\n")
                    y = siguiente(f2)
                    c2 += 1


def mezcla_directa(archivo):
    tam = 1
    pasada = 1
    n = len(leer_todo(archivo))
    while tam < n:
        distribuir(archivo, AUX1, AUX2, tam)
        mezclar(AUX1, AUX2, archivo, tam)
        print(f"Pasada {pasada} (bloques de {tam}): {leer_todo(archivo)}")
        tam *= 2
        pasada += 1


def main():
    datos = [45, 12, 78, 3, 56, 23, 91, 8, 34, 67, 15, 2]
    with open(ARCHIVO, "w") as f:
        for d in datos:
            f.write(f"{d}\n")

    print("=== MEZCLA DIRECTA (ordenamiento externo) ===")
    print("Archivo original:", leer_todo(ARCHIVO), "\n")

    mezcla_directa(ARCHIVO)

    print("\nArchivo ordenado:", leer_todo(ARCHIVO))

    for ruta in (ARCHIVO, AUX1, AUX2):  # limpiar archivos temporales
        os.remove(ruta)


if __name__ == "__main__":
    main()
