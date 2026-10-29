
class Nodo:
    def __init__(self, ingrediente):
        self.ingrediente = ingrediente
        self.siguiente = None


class Postre:
    def __init__(self, nombre):
        self.nombre = nombre
        self.ingredientes = None

    def agregar_ingrediente(self, ingrediente):
        ingrediente = ingrediente.strip().lower()

        if not ingrediente:
            print("El ingrediente no puede estar vacío.")
            return

        actual = self.ingredientes
        anterior = None

        while actual:
            if actual.ingrediente == ingrediente:
                print("Ese ingrediente ya existe.")
                return
            anterior = actual
            actual = actual.siguiente

        nuevo = Nodo(ingrediente)

        if anterior is None:
            self.ingredientes = nuevo
        else:
            anterior.siguiente = nuevo

        print("Ingrediente agregado correctamente.")

    def eliminar_ingrediente(self, ingrediente):
        ingrediente = ingrediente.strip().lower()
        actual = self.ingredientes
        anterior = None

        while actual:
            if actual.ingrediente == ingrediente:
                if anterior is None:
                    self.ingredientes = actual.siguiente
                else:
                    anterior.siguiente = actual.siguiente

                print("Ingrediente eliminado.")
                return

            anterior = actual
            actual = actual.siguiente

        print("El ingrediente no existe.")

    def mostrar_ingredientes(self):
        if self.ingredientes is None:
            print("Este postre no tiene ingredientes.")
            return

        actual = self.ingredientes
        contador = 1

        while actual:
            print(f"{contador}. {actual.ingrediente}")
            actual = actual.siguiente
            contador += 1


POSTRES = []


def buscar_postre(nombre):
    for postre in POSTRES:
        if postre.nombre == nombre.strip().lower():
            return postre
    return None


def agregar_postre():
    nombre = input("Nombre del postre: ").strip().lower()

    if not nombre:
        print("El nombre no puede estar vacío.")
        return

    if buscar_postre(nombre):
        print("El postre ya existe.")
        return

    nuevo = Postre(nombre)

    try:
        cantidad = int(input("Cantidad de ingredientes: "))
        if cantidad < 0:
            print("La cantidad no puede ser negativa.")
            return
    except ValueError:
        print("Debes ingresar un número entero.")
        return

    for i in range(cantidad):
        ingrediente = input(f"Ingrediente {i + 1}: ")
        nuevo.agregar_ingrediente(ingrediente)

    POSTRES.append(nuevo)
    POSTRES.sort(key=lambda postre: postre.nombre)

    print("Postre registrado correctamente.")


def eliminar_postre():
    nombre = input("Nombre del postre a eliminar: ")
    postre = buscar_postre(nombre)

    if postre is None:
        print("El postre no existe.")
        return

    POSTRES.remove(postre)
    print("Postre e ingredientes eliminados.")


def consultar_ingredientes():
    nombre = input("Nombre del postre: ")
    postre = buscar_postre(nombre)

    if postre is None:
        print("El postre no existe.")
        return

    print(f"\nIngredientes de {postre.nombre.title()}:")
    postre.mostrar_ingredientes()


def insertar_ingrediente():
    nombre = input("Nombre del postre: ")
    postre = buscar_postre(nombre)

    if postre is None:
        print("El postre no existe.")
        return

    ingrediente = input("Nuevo ingrediente: ")
    postre.agregar_ingrediente(ingrediente)


def quitar_ingrediente():
    nombre = input("Nombre del postre: ")
    postre = buscar_postre(nombre)

    if postre is None:
        print("El postre no existe.")
        return

    ingrediente = input("Ingrediente a eliminar: ")
    postre.eliminar_ingrediente(ingrediente)


def mostrar_postres():
    if not POSTRES:
        print("No hay postres registrados.")
        return

    print("\nPOSTRES REGISTRADOS")

    for i, postre in enumerate(POSTRES, 1):
        print(f"\n{i}. {postre.nombre.title()}")
        postre.mostrar_ingredientes()


def menu():
    while True:
        print("\n===== MENÚ DE POSTRES =====")
        print("1. Consultar ingredientes")
        print("2. Agregar ingrediente")
        print("3. Eliminar ingrediente")
        print("4. Registrar postre")
        print("5. Eliminar postre")
        print("6. Mostrar todos los postres")
        print("7. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            consultar_ingredientes()
        elif opcion == "2":
            insertar_ingrediente()
        elif opcion == "3":
            quitar_ingrediente()
        elif opcion == "4":
            agregar_postre()
        elif opcion == "5":
            eliminar_postre()
        elif opcion == "6":
            mostrar_postres()
        elif opcion == "7":
            print("Programa finalizado.")
            break
        else:
            print("Opción inválida.")


menu()
