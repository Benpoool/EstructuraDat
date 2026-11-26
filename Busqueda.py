
def convertir_dato(dato):
    try:
        return int(dato)
    except ValueError:
        return dato.lower()


def busqueda_secuencial(lista, objetivo):
    for i in range(len(lista)):
        if lista[i] == objetivo:
            return i
    return -1


def busqueda_binaria(lista, objetivo):
    lista_ordenada = sorted(lista)

    inicio = 0
    final = len(lista_ordenada) - 1

    while inicio <= final:
        medio = (inicio + final) // 2

        if lista_ordenada[medio] == objetivo:
            return medio, lista_ordenada

        elif objetivo < lista_ordenada[medio]:
            final = medio - 1

        else:
            inicio = medio + 1

    return -1, lista_ordenada


def busqueda_hash(lista, objetivo):
    tabla = {}

    for i, dato in enumerate(lista):
        if dato not in tabla:
            tabla[dato] = i

    return tabla.get(objetivo, None)


def menu():
    print("===== LIBRERIA DE BUSQUEDAS =====")

    cantidad = int(input("\n¿Cuantos datos deseas ingresar?: "))

    lista = []

    for i in range(cantidad):
        dato = input(f"Ingresa el dato {i + 1}: ")
        lista.append(convertir_dato(dato))

    while True:
        print("\n===== MENU PRINCIPAL =====")
        print("Lista ingresada:", lista)
        print("1. Busqueda secuencial")
        print("2. Busqueda binaria")
        print("3. Busqueda Hash")
        print("4. Salir")

        opcion = input("\nSelecciona un metodo de busqueda: ")

        if opcion == "1":
            objetivo = convertir_dato(
                input("Ingresa el dato que deseas buscar: ")
            )

            resultado = busqueda_secuencial(lista, objetivo)

            if resultado != -1:
                print(f"Dato encontrado en la posicion {resultado + 1}")
            else:
                print("Dato no encontrado.")

        elif opcion == "2":
            objetivo = convertir_dato(
                input("Ingresa el dato que deseas buscar: ")
            )

            if lista and type(lista[0]) != type(objetivo):
                print("El dato buscado debe ser del mismo tipo que la lista.")
                continue

            resultado, ordenada = busqueda_binaria(lista, objetivo)

            print("Lista ordenada:", ordenada)

            if resultado != -1:
                print(f"Dato encontrado en la posicion {resultado + 1} de la lista ordenada.")
            else:
                print("Dato no encontrado.")

        elif opcion == "3":
            objetivo = convertir_dato(
                input("Ingresa el dato que deseas buscar: ")
            )

            resultado = busqueda_hash(lista, objetivo)

            if resultado is not None:
                print(f"Dato encontrado en la posicion {resultado + 1}")
            else:
                print("Dato no encontrado.")

        elif opcion == "4":
            print("Programa finalizado.")
            break

        else:
            print("Opcion no valida.")


if __name__ == "__main__":
    menu()
