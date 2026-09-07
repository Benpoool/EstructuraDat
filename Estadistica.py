import random
import statistics


class Estadistica:
    def __init__(self, cantidad=50):
        self.cantidad = cantidad
        self.datos = [random.randint(150, 250) for _ in range(cantidad)]

    def calcular_media(self):
        return statistics.mean(self.datos)

    def calcular_mediana(self):
        return statistics.median(self.datos)

    def calcular_moda(self):
        try:
            return statistics.mode(self.datos)
        except statistics.StatisticsError:
            return "No existe una moda única"

    def calcular_varianza(self):
        return statistics.pvariance(self.datos)

    def calcular_desviacion(self):
        return statistics.pstdev(self.datos)

    def mostrar_resultados(self):
        print("Datos generados:")
        print(self.datos)

        print("\n--- RESULTADOS ESTADÍSTICOS ---")
        print(f"Media: {self.calcular_media():.2f}")
        print(f"Mediana: {self.calcular_mediana():.2f}")
        print(f"Moda: {self.calcular_moda()}")
        print(f"Varianza: {self.calcular_varianza():.2f}")
        print(f"Desviación estándar: {self.calcular_desviacion():.2f}")

estadistica = Estadistica(50)

estadistica.mostrar_resultados()