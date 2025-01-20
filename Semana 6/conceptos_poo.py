#Definición de Clase, Definición de Objeto, Herencia, Encapsulación y Polimorfismo en Python para desarrollar un programa
class animal: #Es el padre de las clases
    def __init__(self, nombre, sonido): 
        self.nombre =nombre
        self.sonido= sonido
    def identidad(self):
        return f"El animal es un {self.nombre}"
    def identificacion(self):
        return f"Al animal se lo identifica con su sonido {self.sonido}"
    
class perro(animal):#Herencia
    def __init__(self, nombre, sonido, raza):
        super().__init__(nombre, sonido)
        self.raza= raza
    def obtener_raza(self):# Polimorfismo
        return f"El perro tiene su  raza {self.raza}"
    def imprimir_raza(self):
        return f"Imprime la raza {self.raza}"
    def hacer_sonido(self):
        return "¡Guau!"

class gato(animal):
    def __init__(self, nombre, sonido, color):
        super().__init__(nombre, sonido)  
       # Atributo adicional
        self.__color = color #Encapsulamiento

    def obtener_color(self):
        return self.__color

    # Sobrescritura del método hacer_sonido
    def hacer_sonido(self):
        return "¡Miau!"  
    
#objeto animal ,padre
mi_clase_padre = animal("Perro" , "guau")

#objeto perro
mi_clase_perro= perro("Toby", "Guau", "Pastor Alemán")

#objeto gato
mi_clase_gato= gato("Michu", "Miau", "café")


print(f"El animal es un perro y su nombre es {mi_clase_perro.identidad()} de raza {mi_clase_perro.obtener_raza()} y dice: {mi_clase_perro.hacer_sonido()}")
print(f"El animal es un gato y su nombre es {mi_clase_gato.identidad()} de color {mi_clase_gato.obtener_color()} y dice: {mi_clase_gato.hacer_sonido()}")