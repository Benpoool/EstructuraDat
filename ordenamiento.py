
def shell_sort(lista):
    n = len(lista)
    intervalo = n // 2

    while intervalo > 0:
        for i in range(intervalo, n):
            temp = lista[i]
            j = i

            while j >= intervalo and lista[j - intervalo] > temp:
                lista[j] = lista[j - intervalo]
                j -= intervalo

            lista[j] = temp

        intervalo //= 2

    return lista


def quicksort(lista):
    if len(lista) <= 1:
        return lista

    pivote = lista[len(lista) // 2]

    menores = []
    iguales = []
    mayores = []

    for numero in lista:
        if numero < pivote:
            menores.append(numero)
        elif numero == pivote:
            iguales.append(numero)
        else:
            mayores.append(numero)

    return quicksort(menores) + iguales + quicksort(mayores)


def heapsort(lista):
    n = len(lista)

    def ajustar_heap(n, i):
        mayor = i
        izquierda = 2 * i + 1
        derecha = 2 * i + 2

        if izquierda < n and lista[izquierda] > lista[mayor]:
            mayor = izquierda

        if derecha < n and lista[derecha] > lista[mayor]:
            mayor = derecha

        if mayor != i:
            lista[i], lista[mayor] = lista[mayor], lista[i]
            ajustar_heap(n, mayor)

    # Construir el heap
    for i in range(n // 2 - 1, -1, -1):
        ajustar_heap(n, i)

    # Extraer elementos uno por uno
    for i in range(n - 1, 0, -1):
        lista[0], lista[i] = lista[i], lista[0]
        ajustar_heap(i, 0)

    return lista


def radix_sort(lista):
    if len(lista) == 0:
        return lista

    # Separar negativos y positivos
    negativos = []
    positivos = []

    for numero in lista:
        if numero < 0:
            negativos.append(-numero)
        else:
            positivos.append(numero)

    def ordenar_radix(arr):
        if len(arr) == 0:
            return arr

        maximo = max(arr)
        exp = 1

        while maximo // exp > 0:
            salida = [0] * len(arr)
            conteo = [0] * 10

            for numero in arr:
                digito = (numero // exp) % 10
                conteo[digito] += 1

            for i in range(1, 10):
                conteo[i] += conteo[i - 1]

            for i in range(len(arr) - 1, -1, -1):
                digito = (arr[i] // exp) % 10
                conteo[digito] -= 1
                salida[conteo[digito]] = arr[i]

            arr = salida
            exp *= 10

        return arr

    negativos = ordenar_radix(negativos)
    positivos = ordenar_radix(positivos)

    # Los negativos se invierten para recuperar el orden ascendente
    negativos.reverse()

    resultado_negativos = [-n for n in negativos]

    return resultado_negativos + positivos


def ingresar_numeros():
    while True:
        try:
            cantidad = int(input("\n¿Cuántos números deseas ingresar?: "))

            if cantidad <= 0:
                print("Ingresa una cantidad mayor a cero.")
                continue

            numeros = []

            for i in range(cantidad):
                numero = int(input(f"Ingrese el número {i + 1}: "))
                numeros.append(numero)

            return numeros

        except ValueError:
            print("Error: debes ingresar números enteros.")


def menu():
    while True:
        print("\n========== MENU DE ORDENAMIENTO ==========")
        print("1. ShellSort")
        print("2. Quicksort")
        print("3. Heapsort")
        print("4. Radix Sort")
        print("5. Salir")
        print("======================================")

        opcion = input("Selecciona una opción: ")

        if opcion == "5":
            print("\nPrograma finalizado.")
            break

        if opcion not in ["1", "2", "3", "4"]:
            print("\nOpción no válida. Intenta nuevamente.")
            continue

        numeros = ingresar_numeros()
        original = numeros.copy()

        print("\nNúmeros originales:", original)

        if opcion == "1":
            resultado = shell_sort(numeros)
            nombre = "ShellSort"

        elif opcion == "2":
            resultado = quicksort(numeros)
            nombre = "Quicksort"

        elif opcion == "3":
            resultado = heapsort(numeros)
            nombre = "Heapsort"

        elif opcion == "4":
            resultado = radix_sort(numeros)
            nombre = "Radix Sort"

        print(f"\nMétodo utilizado: {nombre}")
        print("Números ordenados:", resultado)


menu()
