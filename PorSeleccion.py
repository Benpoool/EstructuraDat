def seleccion(lista):
    n = len(lista)

    for i in range(n):
        menor = i

        for j in range(i + 1, n):
            if lista[j] < lista[menor]:
                menor = j

        lista[i], lista[menor] = lista[menor], lista[i]

    return lista


numeros = []

cantidad = int(input("¿Cuántos números deseas ingresar?: "))

for i in range(cantidad):
    numero = int(input(f"Ingrese el número {i + 1}: "))
    numeros.append(numero)

print("\nLista original:", numeros)

resultado = seleccion(numeros.copy())

print("Lista ordenada:", resultado)
