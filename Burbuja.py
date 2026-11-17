def burbuja(lista):
    n = len(lista)

    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]

    return lista


numeros = []

cantidad = int(input("¿Cuántos números deseas ingresar?: "))

for i in range(cantidad):
    numero = int(input(f"Ingrese el número {i + 1}: "))
    numeros.append(numero)

print("\nLista original:", numeros)

resultado = burbuja(numeros.copy())

print("Lista ordenada:", resultado)
