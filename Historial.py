
class Pila:
    def __init__(self):
        self.elementos = []

    def apilar(self, elemento):
        self.elementos.append(elemento)

    def desapilar(self):
        if not self.esta_vacia():
            return self.elementos.pop()
        return None

    def esta_vacia(self):
        return len(self.elementos) == 0

    def vaciar(self):
        self.elementos.clear()


class Navegador:
    def __init__(self):
        self.atras = Pila()
        self.adelante = Pila()
        self.actual = None
        self.historial = []

        self.paginas = [
            ("Google", "https://www.google.com"),
            ("YouTube", "https://www.youtube.com"),
            ("Wikipedia", "https://www.wikipedia.org"),
            ("GitHub", "https://github.com"),
            ("ChatGPT", "https://chatgpt.com")
        ]

    def elegir_pagina(self):
        print("\n--- PAGINAS DISPONIBLES ---")

        for i, (nombre, url) in enumerate(self.paginas, 1):
            print(f"{i}. {nombre}")

        opcion = input("Seleccione una pagina: ")

        if not opcion.isdigit():
            print("Ingrese un numero valido")
            return

        indice = int(opcion) - 1

        if 0 <= indice < len(self.paginas):
            self.visitar(self.paginas[indice])
        else:
            print("Pagina no disponible")

    def visitar(self, pagina):
        if self.actual is not None:
            self.atras.apilar(self.actual)

        self.actual = pagina
        self.adelante.vaciar()
        self.historial.append(pagina)

        nombre, url = pagina
        print(f"\nVisitando: {nombre}")
        print(f"URL: {url}")

    def regresar(self):
        if self.atras.esta_vacia():
            print("No hay paginas anteriores")
        else:
            self.adelante.apilar(self.actual)
            self.actual = self.atras.desapilar()

            nombre, url = self.actual
            print(f"Regresando a: {nombre}")
            print(f"URL: {url}")

    def avanzar(self):
        if self.adelante.esta_vacia():
            print("No hay paginas siguientes")
        else:
            self.atras.apilar(self.actual)
            self.actual = self.adelante.desapilar()

            nombre, url = self.actual
            print(f"Avanzando a: {nombre}")
            print(f"URL: {url}")

    def mostrar_actual(self):
        if self.actual is None:
            print("No hay ninguna pagina abierta")
        else:
            nombre, url = self.actual
            print(f"Pagina actual: {nombre}")
            print(f"URL: {url}")

    def mostrar_historial(self):
        if not self.historial:
            print("El historial esta vacio")
        else:
            print("\n--- HISTORIAL DE VISITAS ---")

            for i, (nombre, url) in enumerate(self.historial, 1):
                print(f"{i}. {nombre} - {url}")


navegador = Navegador()

while True:
    print("\n--- NAVEGADOR WEB ---")
    print("1. Visitar pagina")
    print("2. Regresar")
    print("3. Adelantar")
    print("4. Mostrar pagina actual")
    print("5. Mostrar historial")
    print("6. Salir")

    opcion = input("Seleccione una opcion: ")

    if opcion == "1":
        navegador.elegir_pagina()

    elif opcion == "2":
        navegador.regresar()

    elif opcion == "3":
        navegador.avanzar()

    elif opcion == "4":
        navegador.mostrar_actual()

    elif opcion == "5":
        navegador.mostrar_historial()

    elif opcion == "6":
        print("Cerrando navegador...")
        break

    else:
        print("Opcion no valida")
