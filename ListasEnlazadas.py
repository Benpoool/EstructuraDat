
class Nodo:
    def __init__(self, info):
        self.info = info
        self.liga = None


def recorrer(P):
    if P is None:
        print("\nLa lista está vacía.")
        return

    actual = P
    print("\nLista simplemente ligada:")

    while actual is not None:
        print(actual.info, end=" -> ")
        actual = actual.liga

    print("None")


def contar_nodos(P):
    contador = 0
    actual = P

    while actual is not None:
        contador += 1
        actual = actual.liga

    return contador


def mostrar_posiciones(P):
    actual = P
    posicion = 1

    print("\nLista actual con posiciones:")

    while actual is not None:
        print(f"[{posicion}: {actual.info}]", end=" -> ")
        actual = actual.liga
        posicion += 1

    print("None")


def insertar_inicio(P, info):
    Q = Nodo(info)
    Q.liga = P
    P = Q
    return P


def insertar_final(P, info):
    Q = Nodo(info)

    if P is None:
        return Q

    actual = P

    while actual.liga is not None:
        actual = actual.liga

    actual.liga = Q
    return P


def insertar_intermedio(P, info, posicion):
    Q = Nodo(info)
    actual = P

    for i in range(posicion - 2):
        actual = actual.liga

    Q.liga = actual.liga
    actual.liga = Q

    return P



def insertar(P):
    print("\n--- INSERTAR ELEMENTO ---")

    print("\n¿Dónde desea insertar el nuevo nodo?")
    print("1. Al inicio")
    print("2. Al final")
    print("3. En una posición intermedia")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        info = input("Ingrese el valor del nuevo nodo: ")
        P = insertar_inicio(P, info)

    elif opcion == "2":
        info = input("Ingrese el valor del nuevo nodo: ")
        P = insertar_final(P, info)

    elif opcion == "3":
        cantidad = contar_nodos(P)

        if cantidad < 2:
            print("\nSe necesitan al menos 2 nodos para insertar entre ellos.")
            return P

        mostrar_posiciones(P)

        print(f"\nPosiciones intermedias disponibles: 2 a {cantidad}")

        try:
            posicion = int(input("Elija una posición numerada: "))
        except ValueError:
            print("\nDebe ingresar un número entero.")
            return P

        if posicion < 2 or posicion > cantidad:
            print("\nPosición no válida.")
            return P

        info = input("Ingrese el valor del nuevo nodo: ")
        P = insertar_intermedio(P, info, posicion)

    else:
        print("\nOpción no válida.")
        return P

    print("\nNodo insertado correctamente.")
    recorrer(P)

    return P



def borrar(P):
    if P is None:
        print("\nLa lista está vacía.")
        return P

    mostrar_posiciones(P)
    cantidad = contar_nodos(P)

    try:
        posicion = int(input("\nSeleccione la posición del nodo a borrar: "))
    except ValueError:
        print("\nDebe ingresar un número entero.")
        return P

    if posicion < 1 or posicion > cantidad:
        print("\nPosición no válida.")
        return P

    if posicion == 1:
        P = P.liga

    else:
        actual = P

        for i in range(posicion - 2):
            actual = actual.liga

        actual.liga = actual.liga.liga

    print("\nNodo eliminado correctamente.")
    recorrer(P)

    return P


def buscar(P):
    if P is None:
        print("\nLa lista está vacía.")
        return

    info = input("\nIngrese el valor que desea buscar: ")

    actual = P
    posicion = 1
    encontrado = False

    while actual is not None:
        if actual.info == info:
            print(f"Elemento encontrado en la posición {posicion}.")
            encontrado = True

        actual = actual.liga
        posicion += 1

    if not encontrado:
        print("\nEl elemento no existe en la lista.")


def crea_inicio():
    print("===== CREACIÓN DE LA LISTA =====")

    info = input("Ingrese el valor del primer nodo: ")
    P = Nodo(info)

    recorrer(P)

    while True:
        RES = input("\n¿Desea ingresar otro nodo? Sí: 1, No: 0: ")

        if RES == "0":
            break

        elif RES == "1":
            P = insertar(P)

        else:
            print("\nIngrese solamente 1 o 0.")

    print("\nLista creada correctamente.")
    recorrer(P)

    return P


def menu():
    P = crea_inicio()

    while True:
        print("\n===== LISTA SIMPLEMENTE LIGADA =====")
        print("1. Recorrer lista")
        print("2. Insertar elemento")
        print("3. Borrar elemento")
        print("4. Buscar elemento")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            recorrer(P)

        elif opcion == "2":
            P = insertar(P)

        elif opcion == "3":
            P = borrar(P)

        elif opcion == "4":
            buscar(P)

        elif opcion == "5":
            print("\nPrograma finalizado.")
            break

        else:
            print("\nOpción no válida.")


menu()
