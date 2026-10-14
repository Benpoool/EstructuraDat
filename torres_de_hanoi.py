from time import perf_counter


def hanoi(discos, origen, auxiliar, destino, mostrar=False):
    """Resuelve el problema recursivamente; devuelve la cantidad de movimientos."""
    if discos == 0:
        return 0
    movimientos = hanoi(discos - 1, origen, destino, auxiliar, mostrar)
    if mostrar:
        print(f"Mover disco {discos}: {origen} -> {destino}")
    movimientos += 1
    movimientos += hanoi(discos - 1, auxiliar, origen, destino, mostrar)
    return movimientos


def medir_tiempo(discos, limite_segundos=3.0):
    """Cronometra una ejecucion real; si supera el limite, la detiene con una excepcion."""
    inicio = perf_counter()
    movimientos = 0

    def recorrer(n):
        nonlocal movimientos
        if n == 0:
            return
        if perf_counter() - inicio >= limite_segundos:
            raise TimeoutError
        recorrer(n - 1)
        movimientos += 1
        recorrer(n - 1)

    try:
        recorrer(discos)
        return perf_counter() - inicio, movimientos, True
    except TimeoutError:
        return perf_counter() - inicio, movimientos, False


def main():
    print("TORRES DE HANOI - PRUEBAS DE RENDIMIENTO")
    print("El algoritmo tiene 2**n - 1 movimientos minimos.\n")
    print(" n | movimientos requeridos | segundos observados | resultado")
    print("-" * 78)
    for n in (5, 10, 30, 64):
        total = (1 << n) - 1
        tiempo, hechos, termino = medir_tiempo(n, limite_segundos=3.0)
        if termino:
            detalle = "completado"
            tiempo_texto = f"{tiempo:.6f}"
        else:
            detalle = f"interrumpido tras {hechos:,} movimientos"
            tiempo_texto = f"> {tiempo:.3f}"
        print(f"{n:2} | {total:20,} | {tiempo_texto:18} | {detalle}")
    print("\nNOTA: los casos interrumpidos NO tienen un tiempo total medido.")
    print("Para estimar el tiempo de 30 o 64 discos usa como referencia")
    print("una prueba completada: T(n) ~= T(k)*(2**n-1)/(2**k-1).")
    print("La estimacion es orientativa y NO equivale a ejecutar el caso completo.")


if __name__ == "__main__":
    main()
