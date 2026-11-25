"""
Problema: ordenar el archivo de ventas diarias (montos) de una tienda usando
cuatro archivos: F1 y F2 (entrada) y G1 y G2 (salida). Se aprovechan las
secuencias ya ordenadas que existen de forma natural (corridas) y en cada
pasada los archivos de entrada y salida intercambian su función.
"""
import os

ARCHIVO = "ventas.txt"
F1, F2, G1, G2 = "f1.txt", "f2.txt", "g1.txt", "g2.txt"


class Lector:

    def __init__(self, ruta):
        self.f = open(ruta)
        self.actual = self._leer()

    def _leer(self):
        linea = self.f.readline()
        return int(linea) if linea.strip() else None

    def avanzar(self):
        valor = self.actual
        self.actual = self._leer()
        return valor

    def cerrar(self):
        self.f.close()


def leer_todo(ruta):
    with open(ruta) as f:
        return [int(x) for x in f.read().split()]


def distribuir_corridas(origen, f1, f2):
    with open(origen) as f, open(f1, "w") as a, open(f2, "w") as b:
        destino = a
        anterior = None
        for linea in f:
            valor = int(linea)
            if anterior is not None and valor < anterior:  # terminó una corrida
                destino = b if destino is a else a
            destino.write(f"{valor}\n")
            anterior = valor


def en_corrida(lector, ultimo):
    return lector.actual is not None and (ultimo is None or lector.actual >= ultimo)


def mezclar_corrida(l1, l2, out):
    ult1 = ult2 = None
    while en_corrida(l1, ult1) or en_corrida(l2, ult2):
        toma_1 = en_corrida(l1, ult1) and (
            not en_corrida(l2, ult2) or l1.actual <= l2.actual
        )
        if toma_1:
            ult1 = l1.avanzar()
            out.write(f"{ult1}\n")
        else:
            ult2 = l2.avanzar()
            out.write(f"{ult2}\n")


def mezcla_equilibrada(archivo):
    entrada = (F1, F2)
    salida = (G1, G2)
    distribuir_corridas(archivo, *entrada)
    print("Distribución inicial de corridas:")
    print("  F1:", leer_todo(F1))
    print("  F2:", leer_todo(F2))

    pasada = 1
    while True:
        l1, l2 = Lector(entrada[0]), Lector(entrada[1])
        with open(salida[0], "w") as s1, open(salida[1], "w") as s2:
            destino = s1
            while l1.actual is not None or l2.actual is not None:
                mezclar_corrida(l1, l2, destino)
                destino = s2 if destino is s1 else s1
        l1.cerrar()
        l2.cerrar()

        print(f"\nPasada {pasada}:")
        print(f"  {salida[0]}:", leer_todo(salida[0]))
        print(f"  {salida[1]}:", leer_todo(salida[1]))

        # Si un archivo de salida quedó vacío, el otro contiene todo ordenado
        if os.path.getsize(salida[1]) == 0:
            return salida[0]
        if os.path.getsize(salida[0]) == 0:
            return salida[1]

        entrada, salida = salida, entrada  # intercambian funciones
        pasada += 1


def main():
    datos = [34, 56, 12, 89, 5, 23, 67, 41, 90, 8, 15, 72, 3, 60]
    with open(ARCHIVO, "w") as f:
        for d in datos:
            f.write(f"{d}\n")

    print("=== MEZCLA EQUILIBRADA (4 archivos, corridas naturales) ===")
    print("Archivo original:", leer_todo(ARCHIVO), "\n")

    resultado = mezcla_equilibrada(ARCHIVO)
    print("\nArchivo ordenado:", leer_todo(resultado))

    for ruta in (ARCHIVO, F1, F2, G1, G2):  # limpiar archivos temporales
        os.remove(ruta)


if __name__ == "__main__":
    main()
