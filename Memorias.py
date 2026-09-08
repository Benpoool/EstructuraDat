def MemoriaEstatica():
    calificaciones=[0]*5
    for i in range(len(calificaciones)):
        calificaciones[i] = int(input("Introduce las calificaciones: "))
    print(calificaciones)
        
def MemoriaDinamica():
    frutas = []
    frutas.append("Mango")
    frutas.append("Manzana")
    frutas.append("Banana")
    frutas.append("Uvas")
    print(frutas)
    frutas.pop(0)
    frutas.pop(1)
    frutas.append("sandia")
    print(frutas)

MemoriaEstatica()    
MemoriaDinamica()