#POO
class Semana: #Clase que representa una semana y permite gestionar temperaturas diarias.
    def __init__(self):#Constructor de la clase Semana
        self.temperaturas = []#Se inicializa la lista vacia mpara almacenar las temperaturas

    def agregar_temperatura(self, temperatura):#Método para agregar una temperatura a la lista de temperaturas.
        self.temperaturas.append(temperatura)

    def calcular_promedio(self):# Método para calcular el promedio de las temperaturas almacenadas.
        if not self.temperaturas:# Se verifica si la lista de temperaturas está vacía
            return "No se han ingresado temperaturas."
        promedio = sum(self.temperaturas) / len(self.temperaturas)#Se calcula el promedio sumando las temperaturas y dividiendo entre el total de las temperaturas.
        return f"El promedio semanal de temperatura es: {promedio:.2f}°C"

if __name__ == "__main__":
    semana = Semana()#Se crea instancia de la clase Semana.
    for dia in range(1, 8):#Bucle para solicitar la temperatura de cada dia de la semana
        temperatura = float(input(f"Ingrese la temperatura del día {dia}:" ))#Le solicita al usuario la temperatura y la convierte en float
        semana.agregar_temperatura(temperatura) # Agrega la temperatura a la lista en la instancia de la clase Semana.
    print(semana.calcular_promedio())#Imprime el promedio semanal


