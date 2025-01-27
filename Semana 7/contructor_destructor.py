# Implementación de Constructores y Destructores en Python
class Estudiante:
    def __init__(self, nombre,apellido , matricula, carrera):#Constructor de la clase Estudiante.
    
        self.nombre = nombre
        self.apellido = apellido
        self.matricula = matricula
        self.carrera = carrera
        print(f"Se ha registrado al estudiante: {self.nombre}{self.apellido} ({self.matricula}), inscrito en la carrera {self.carrera}.")
    
    def mostrar_informacion(self):#Método para mostrar la información del estudiante.
        print(f"Nombre: {self.nombre}")
        print(f"Apellido: {self.apellido}")
        print(f"Matrícula: {self.matricula}")
        print(f"Carrera: {self.carrera}")
    
    def __del__(self):#Destructor de la clase Estudiante.
        print(f"Se ha eliminado el registro del estudiante: {self.nombre} ({self.matricula}).")

# Crear un objeto de la clase Estudiante
estudiante1 = Estudiante("Anayely", "Quezada", "A2345R", "Tecnologías de la información")

# Mostrar la información del estudiante
estudiante1.mostrar_informacion()

# El objeto estudiante1 será destruido cuando termine el programa