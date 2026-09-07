class vectores:
    def mostrarVector(self, datos):
        for i in range(len(datos)):
            print(datos[i])
            
    def media(self, datos):
        suma=0
        for i in range(len(datos)):
            suma=suma+datos[i]
        return suma/len(datos)
            
pares= [2,4,6,8,10]
impares= [1,3,5,7,9]
v = vectores()
v.mostrarVector(pares)
print("Media= " + str(v.media(pares)))
v.mostrarVector(impares)
print("Media= " + str(v.media(impares)))