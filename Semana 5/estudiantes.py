
# Gestiona un registro de estudiantes.
#El usuario puede agregar un estudiante con su nombre, edad, y calificación promedio.
#El programa valida los datos ingresados y muestra un resumen del registro al final.


# Función para agregar un estudiante al registro
def agregar_estudiante(registro, nombre, edad, promedio):#Agrega un estudiante al registro.Para registro: Lista que contiene el registro de estudiantes (list).Para nombre: Nombre del estudiante (string). Param edad: Edad del estudiante (integer)
                                                         #para promedio: Promedio del estudiante (float)
    estudiante = {
        "nombre": nombre,
        "edad": edad,
        "promedio": promedio
    }
    registro.append(estudiante)

# Registro principal de estudiantes (lista)
registro_estudiantes = []

# Bucle para gestionar la entrada de datos
while True:
    print("\n--- Registro de Estudiantes ---")
    
    # Entrada de datos del estudiante
    nombre_estudiante = input("Ingrese el nombre del estudiante: ")
    edad_estudiante = int(input("Ingrese la edad del estudiante: "))
    promedio_estudiante = float(input("Ingrese el promedio del estudiante: "))
    
    # Validación básica de datos
    if edad_estudiante > 0 and 0.0 <= promedio_estudiante <= 10.0:
        agregar_estudiante(registro_estudiantes, nombre_estudiante, edad_estudiante, promedio_estudiante)
        print(f"Estudiante {nombre_estudiante} Estudiante agregado.")
    else:
        print("Error: Verifique que la edad sea positiva y el promedio esté entre 0.0 y 10.0.")
    
    # Preguntar al usuario si desea agregar otro estudiante
    continuar = input("¿Desea agregar otro estudiante? (sí/no): ").strip().lower()
    if continuar != "sí":
        break

# Mostrar resumen del registro
print("\n--- Resumen del Registro de Estudiantes ---")
for idx, estudiante in enumerate(registro_estudiantes, start=1):
    print(f"Estudiante {idx}: Nombre: {estudiante['nombre']}, Edad: {estudiante['edad']}, Promedio: {estudiante['promedio']:.2f}")

# Indicar si el registro está vacío
if not registro_estudiantes:
    print("El registro está vacío.")
else:
    print(f"Total de estudiantes registrados: {len(registro_estudiantes)}")
