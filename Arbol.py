
import tkinter as tk
from tkinter import ttk


# CLASE NODO
class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.izquierda = None
        self.derecha = None


# CLASE ARBOL
class Arbol:
    def __init__(self):
        self.raiz = None

    def esta_vacio(self):
        return self.raiz is None

    def insertar(self, dato):
        nuevo = Nodo(dato)

        if self.esta_vacio():
            self.raiz = nuevo
        else:
            self._insertar(self.raiz, nuevo)

    def _insertar(self, actual, nuevo):
        if nuevo.dato < actual.dato:
            if actual.izquierda is None:
                actual.izquierda = nuevo
            else:
                self._insertar(actual.izquierda, nuevo)
        else:
            if actual.derecha is None:
                actual.derecha = nuevo
            else:
                self._insertar(actual.derecha, nuevo)

    def buscar(self, actual, dato):
        if actual is None:
            return False

        if actual.dato == dato:
            return True

        if dato < actual.dato:
            return self.buscar(actual.izquierda, dato)

        return self.buscar(actual.derecha, dato)

    # OBTENER NODOS SEGUN EL TIPO DE RECORRIDO
    def recorrido(self, actual, tipo, resultado):
        if actual is None:
            return

        if tipo == "Preorden":
            resultado.append(actual)

        self.recorrido(actual.izquierda, tipo, resultado)

        if tipo == "Inorden":
            resultado.append(actual)

        self.recorrido(actual.derecha, tipo, resultado)

        if tipo == "Posorden":
            resultado.append(actual)


# INTERFAZ GRAFICA
class Aplicacion:
    def __init__(self, ventana):
        self.arbol = Arbol()
        self.ventana = ventana

        self.ventana.title("Arbol Binario de Busqueda")
        self.ventana.geometry("1050x800")
        self.ventana.minsize(800, 650)

        # VARIABLES DE ANIMACION
        self.nodos_recorrido = []
        self.paso = 0
        self.visitados = set()
        self.nodo_actual = None
        self.temporizador = None

        self.crear_interfaz()

    def crear_interfaz(self):

        # TITULO
        ttk.Label(
            self.ventana,
            text="ARBOL BINARIO DE BUSQUEDA",
            font=("Arial", 19, "bold")
        ).pack(pady=15)

        # ENTRADA DE DATOS
        panel = ttk.Frame(self.ventana)
        panel.pack(pady=10)

        ttk.Label(
            panel, text="Valor:"
        ).grid(row=0, column=0, padx=5)

        self.entrada = ttk.Entry(panel, width=15)
        self.entrada.grid(row=0, column=1, padx=5)

        ttk.Button(
            panel,
            text="Insertar",
            command=self.insertar
        ).grid(row=0, column=2, padx=5)

        ttk.Button(
            panel,
            text="Buscar",
            command=self.buscar
        ).grid(row=0, column=3, padx=5)

        # SELECCION DE RECORRIDOS
        marco = ttk.LabelFrame(
            self.ventana,
            text="Seleccionar recorrido"
        )
        marco.pack(pady=10)

        for columna, tipo in enumerate(
            ["Inorden", "Preorden", "Posorden"]
        ):
            ttk.Button(
                marco,
                text=tipo,
                command=lambda t=tipo: self.iniciar_recorrido(t)
            ).grid(row=0, column=columna, padx=12, pady=10)

        # VELOCIDAD DE ANIMACION
        controles = ttk.LabelFrame(
            self.ventana,
            text="Velocidad de animacion"
        )
        controles.pack(pady=8)

        self.velocidad = ttk.Combobox(
            controles,
            values=["Lenta", "Normal", "Rapida"],
            state="readonly",
            width=12
        )
        self.velocidad.set("Normal")
        self.velocidad.pack(padx=10, pady=8)

        # MENSAJES
        self.mensaje = ttk.Label(
            self.ventana,
            text="Inserta valores para construir el arbol.",
            font=("Arial", 11)
        )
        self.mensaje.pack(pady=8)

        self.progreso = ttk.Label(
            self.ventana,
            text="Paso: 0 / 0",
            font=("Arial", 12, "bold")
        )
        self.progreso.pack(pady=5)

        self.resultado = ttk.Label(
            self.ventana,
            text="",
            font=("Arial", 11)
        )
        self.resultado.pack(pady=5)

        # LEYENDA DE COLORES
        leyenda = ttk.Frame(self.ventana)
        leyenda.pack(pady=5)

        colores = [
            ("#2563eb", "Pendiente"),
            ("#eab308", "Visitando"),
            ("#16a34a", "Visitado")
        ]

        for color, texto in colores:
            tk.Label(
                leyenda,
                text="   ",
                bg=color
            ).pack(side="left", padx=(8, 2))

            ttk.Label(
                leyenda,
                text=texto
            ).pack(side="left")

        # AREA GRAFICA
        marco_arbol = ttk.LabelFrame(
            self.ventana,
            text="Visualizacion del arbol"
        )
        marco_arbol.pack(
            fill="both",
            expand=True,
            padx=15,
            pady=10
        )

        self.canvas = tk.Canvas(
            marco_arbol,
            bg="white"
        )

        barra_x = ttk.Scrollbar(
            marco_arbol,
            orient="horizontal",
            command=self.canvas.xview
        )

        barra_y = ttk.Scrollbar(
            marco_arbol,
            orient="vertical",
            command=self.canvas.yview
        )

        self.canvas.configure(
            xscrollcommand=barra_x.set,
            yscrollcommand=barra_y.set
        )

        self.canvas.grid(
            row=0, column=0, sticky="nsew"
        )

        barra_y.grid(
            row=0, column=1, sticky="ns"
        )

        barra_x.grid(
            row=1, column=0, sticky="ew"
        )

        marco_arbol.rowconfigure(0, weight=1)
        marco_arbol.columnconfigure(0, weight=1)

        self.dibujar_arbol()

    # DETENER ANIMACION ANTERIOR
    def detener_temporizador(self):
        if self.temporizador is not None:
            self.ventana.after_cancel(self.temporizador)
            self.temporizador = None

    # INSERTAR NODO
    def insertar(self):
        self.detener_temporizador()

        try:
            dato = int(self.entrada.get())

            self.arbol.insertar(dato)
            self.entrada.delete(0, tk.END)

            self.limpiar_recorrido()
            self.dibujar_arbol()

            self.mensaje.config(
                text=f"Nodo {dato} insertado correctamente."
            )

        except ValueError:
            self.mensaje.config(
                text="Ingresa un numero entero valido."
            )

    # BUSCAR NODO
    def buscar(self):
        self.detener_temporizador()

        if self.arbol.esta_vacio():
            self.mensaje.config(
                text="El arbol esta vacio."
            )
            return

        try:
            dato = int(self.entrada.get())

            encontrado = self.arbol.buscar(
                self.arbol.raiz, dato
            )

            self.limpiar_recorrido()

            if encontrado:
                self.mensaje.config(
                    text=f"El valor {dato} fue encontrado."
                )
                self.dibujar_arbol(buscado=dato)

            else:
                self.mensaje.config(
                    text=f"El valor {dato} no existe."
                )
                self.dibujar_arbol()

        except ValueError:
            self.mensaje.config(
                text="Ingresa un numero entero valido."
            )

    # INICIAR RECORRIDO AUTOMATICO
    def iniciar_recorrido(self, tipo):
        self.detener_temporizador()

        if self.arbol.esta_vacio():
            self.mensaje.config(
                text="No se puede recorrer un arbol vacio."
            )
            return

        self.nodos_recorrido = []

        self.arbol.recorrido(
            self.arbol.raiz,
            tipo,
            self.nodos_recorrido
        )

        self.tipo = tipo
        self.paso = 0
        self.visitados = set()
        self.nodo_actual = None

        self.resultado.config(text="")

        self.mostrar_siguiente()

    # MOSTRAR CADA NODO DEL RECORRIDO
    def mostrar_siguiente(self):

        if self.paso >= len(self.nodos_recorrido):
            self.nodo_actual = None
            self.dibujar_arbol()

            self.mensaje.config(
                text="Recorrido terminado."
            )

            self.resultado.config(
                text=f"{self.tipo}: " +
                " - ".join(
                    str(n.dato) for n in self.nodos_recorrido
                )
            )

            self.progreso.config(
                text=f"Paso: {len(self.nodos_recorrido)} / "
                f"{len(self.nodos_recorrido)}"
            )

            self.temporizador = None
            return

        self.nodo_actual = self.nodos_recorrido[self.paso]

        self.visitados.add(id(self.nodo_actual))

        self.mensaje.config(
            text=f"Visitando nodo: {self.nodo_actual.dato}"
        )

        self.progreso.config(
            text=f"Paso: {self.paso + 1} / "
            f"{len(self.nodos_recorrido)}"
        )

        self.dibujar_arbol()

        self.paso += 1

        tiempos = {
            "Lenta": 1500,
            "Normal": 800,
            "Rapida": 300
        }

        tiempo = tiempos.get(
            self.velocidad.get(), 800
        )

        self.temporizador = self.ventana.after(
            tiempo,
            self.mostrar_siguiente
        )

    # LIMPIAR RECORRIDO ANTERIOR
    def limpiar_recorrido(self):
        self.nodos_recorrido = []
        self.paso = 0
        self.visitados.clear()
        self.nodo_actual = None

        self.progreso.config(text="Paso: 0 / 0")
        self.resultado.config(text="")

    # DIBUJAR ARBOL
    def dibujar_arbol(self, buscado=None):
        self.canvas.delete("all")

        if self.arbol.esta_vacio():
            self.canvas.create_text(
                400, 200,
                text="Arbol vacio",
                font=("Arial", 18),
                fill="gray"
            )

            self.canvas.configure(
                scrollregion=(0, 0, 900, 450)
            )
            return

        posiciones = {}
        contador = [0]
        profundidad = [0]

        # CALCULAR POSICIONES
        def asignar_posiciones(nodo, nivel):
            if nodo is None:
                return

            asignar_posiciones(
                nodo.izquierda, nivel + 1
            )

            x = 60 + contador[0] * 90
            y = 60 + nivel * 100

            posiciones[id(nodo)] = (x, y)

            contador[0] += 1
            profundidad[0] = max(
                profundidad[0], nivel
            )

            asignar_posiciones(
                nodo.derecha, nivel + 1
            )

        asignar_posiciones(
            self.arbol.raiz, 0
        )

        ancho = max(
            900, contador[0] * 90 + 120
        )

        alto = max(
            450, (profundidad[0] + 1) * 100 + 100
        )

        self.canvas.configure(
            scrollregion=(0, 0, ancho, alto)
        )

        # DIBUJAR CONEXIONES
        def lineas(nodo):
            if nodo is None:
                return

            x, y = posiciones[id(nodo)]

            for hijo in [
                nodo.izquierda,
                nodo.derecha
            ]:
                if hijo is not None:
                    hx, hy = posiciones[id(hijo)]

                    self.canvas.create_line(
                        x, y, hx, hy,
                        fill="#64748b",
                        width=2
                    )

            lineas(nodo.izquierda)
            lineas(nodo.derecha)

        lineas(self.arbol.raiz)

        # DIBUJAR NODOS
        def nodos(nodo):
            if nodo is None:
                return

            x, y = posiciones[id(nodo)]

            if nodo is self.nodo_actual:
                color = "#eab308"

            elif id(nodo) in self.visitados:
                color = "#16a34a"

            elif nodo.dato == buscado:
                color = "#16a34a"

            else:
                color = "#2563eb"

            self.canvas.create_oval(
                x - 23, y - 23,
                x + 23, y + 23,
                fill=color,
                outline="#1e293b",
                width=2
            )

            self.canvas.create_text(
                x, y,
                text=str(nodo.dato),
                fill="white",
                font=("Arial", 11, "bold")
            )

            nodos(nodo.izquierda)
            nodos(nodo.derecha)

        nodos(self.arbol.raiz)


# EJECUTAR PROGRAMA
ventana = tk.Tk()
app = Aplicacion(ventana)
ventana.mainloop()
