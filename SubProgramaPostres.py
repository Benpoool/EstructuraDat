class Nodo:
    def __init__(self, ingrediente):
        self.ingrediente = ingrediente
        self.siguiente = None


class Postre:
    def __init__(self, nombre):
        self.nombre = nombre
        self.ingredientes = None

    def agregar_ingrediente(self, ingrediente):
        nuevo = Nodo(ingrediente.strip().lower())

        if self.ingredientes is None:
            self.ingredientes = nuevo
        else:
            actual = self.ingredientes

            while actual.siguiente is not None:
                actual = actual.siguiente

            actual.siguiente = nuevo

    def mostrar_ingredientes(self):
        if self.ingredientes is None:
            print("No hay ingredientes.")
            return

        actual = self.ingredientes
        posicion = 1

        while actual is not None:
            print(f"{posicion}. {actual.ingrediente}")
            actual = actual.siguiente
            posicion += 1

    def eliminar_repetidos(self):
        actual = self.ingredientes
        encontrados = set()
        anterior = None
        eliminados = 0

        while actual is not None:
            if actual.ingrediente in encontrados:
                anterior.siguiente = actual.siguiente
                actual = anterior.siguiente
                eliminados += 1
            else:
                encontrados.add(actual.ingrediente)
                anterior = actual
                actual = actual.siguiente

        return eliminados


POSTRES = []


def buscar_postre(nombre):
    for postre in POSTRES:
        if postre.nombre == nombre.strip().lower():
            return postre
    return None


def registrar_postre():
    nombre = input("Nombre del postre: ").strip().lower()

    if not nombre:
        print("El nombre no puede estar vacío.")
        return

    if buscar_postre(nombre):
        print("El postre ya existe.")
        return

    try:
        cantidad = int(input("Cantidad de ingredientes: "))

        if cantidad < 0:
            print("La cantidad no puede ser negativa.")
            return

    except ValueError:
        print("Debes ingresar un número válido.")
        return

    nuevo = Postre(nombre)

    for i in range(cantidad):
        ingrediente = input(f"Ingrediente {i + 1}: ").strip()

        if ingrediente:
            nuevo.agregar_ingrediente(ingrediente)
        else:
            print("Ingrediente vacío, no se agregó.")

    POSTRES.append(nuevo)
    POSTRES.sort(key=lambda postre: postre.nombre)

    print("Postre registrado correctamente.")


def mostrar_postres():
    if not POSTRES:
        print("No hay postres registrados.")
        return

    print("\n===== LISTA DE POSTRES =====")

    for postre in POSTRES:
        print(f"\nPostre: {postre.nombre.title()}")
        postre.mostrar_ingredientes()


def eliminar_todos_repetidos():
    if not POSTRES:
        print("No hay postres registrados.")
        return

    total = 0

    for postre in POSTRES:
        eliminados = postre.eliminar_repetidos()
        total += eliminados

        print(f"\nPostre: {postre.nombre.title()}")
        print(f"Ingredientes repetidos eliminados: {eliminados}")

    print(f"\nTotal de elementos eliminados: {total}")


def menu():
    while True:
        print("\n===== MENÚ DE POSTRES =====")
        print("1. Registrar postre")
        print("2. Mostrar postres e ingredientes")
        print("3. Eliminar ingredientes repetidos")
        print("4. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            registrar_postre()

        elif opcion == "2":
            mostrar_postres()

        elif opcion == "3":
            eliminar_todos_repetidos()

        elif opcion == "4":
            print("Programa finalizado.")
            break

        else:
            print("Opción inválida.")


menu()