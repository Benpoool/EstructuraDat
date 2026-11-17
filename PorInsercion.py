def insercion(lista):
    for i in range(1, len(lista)):
        actual = lista[i]
        j = i - 1

        while j >= 0 and lista[j] > actual:
            lista[j + 1] = lista[j]
            j -= 1

        lista[j + 1] = actual

    return lista


numeros = []

cantidad = int(input("¿Cuántos números deseas ingresar?: "))

for i in range(cantidad):
    numero = int(input(f"Ingrese el número {i + 1}: "))
    numeros.append(numero)

print("\nLista original:", numeros)

resultado = insercion(numeros.copy())

print("Lista ordenada:", resultado)
