class Cola:
    def __init__(self):
        self.elementos = []

    def encolar(self, elemento):
        self.elementos.append(elemento)

    def desencolar(self):
        if not self.esta_vacia():
            return self.elementos.pop(0)
        return None

    def esta_vacia(self):
        return len(self.elementos) == 0

    def mostrar(self):
        return self.elementos


def sumar_colas(cola_a, cola_b):
    resultado = Cola()

    if len(cola_a.elementos) != len(cola_b.elementos):
        print("Error: Las colas deben tener el mismo tamaño.")
        return resultado

    for a, b in zip(cola_a.elementos, cola_b.elementos):
        resultado.encolar(a + b)

    return resultado


cola_a = Cola()
cola_b = Cola()

for numero in [3, 4, 2, 8, 12]:
    cola_a.encolar(numero)

for numero in [6, 2, 9, 11, 3]:
    cola_b.encolar(numero)

cola_resultado = sumar_colas(cola_a, cola_b)

print("Cola A\tCola B\tCola resultado")

for a, b, r in zip(
    cola_a.mostrar(),
    cola_b.mostrar(),
    cola_resultado.mostrar()
):
    print(f"{a}\t{b}\t{r}")
