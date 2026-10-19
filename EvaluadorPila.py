class Pila:
    def __init__(self):
        self.elementos = []

    def apilar(self, elemento):
        self.elementos.append(elemento)

    def desapilar(self):
        if not self.esta_vacia():
            return self.elementos.pop()
        raise ValueError("La pila esta vacia")

    def esta_vacia(self):
        return len(self.elementos) == 0


def operar(a, b, operador):
    if operador == "+":
        return a + b
    elif operador == "-":
        return a - b
    elif operador == "*":
        return a * b
    elif operador == "/":
        if b == 0:
            raise ZeroDivisionError("No se puede dividir entre cero")
        return a / b
    elif operador == "^":
        return a ** b


def evaluar_posfija(expresion):
    pila = Pila()
    operadores = ["+", "-", "*", "/", "^"]

    for elemento in expresion.split():
        if elemento in operadores:
            b = pila.desapilar()
            a = pila.desapilar()
            resultado = operar(a, b, elemento)
            pila.apilar(resultado)
        else:
            pila.apilar(float(elemento))

    resultado = pila.desapilar()

    if not pila.esta_vacia():
        raise ValueError("Expresion incorrecta")

    return resultado


def evaluar_prefija(expresion):
    pila = Pila()
    operadores = ["+", "-", "*", "/", "^"]

    for elemento in reversed(expresion.split()):
        if elemento in operadores:
            a = pila.desapilar()
            b = pila.desapilar()
            resultado = operar(a, b, elemento)
            pila.apilar(resultado)
        else:
            pila.apilar(float(elemento))

    resultado = pila.desapilar()

    if not pila.esta_vacia():
        raise ValueError("Expresion incorrecta")

    return resultado


while True:
    print("\n--- EVALUADOR DE EXPRESIONES ---")
    print("1. Evaluar expresion posfija")
    print("2. Evaluar expresion prefija")
    print("3. Salir")

    opcion = input("Seleccione una opcion: ")

    if opcion == "3":
        print("Programa finalizado")
        break

    if opcion == "1" or opcion == "2":
        expresion = input("Ingrese la expresion separada por espacios: ")

        try:
            if opcion == "1":
                resultado = evaluar_posfija(expresion)
            else:
                resultado = evaluar_prefija(expresion)

            print("Resultado:", resultado)

        except (ValueError, ZeroDivisionError) as error:
            print("Error:", error)
    else:
        print("Opcion no valida")
