#Programacion tradiccional
#Se crea auna función para crear el promedio semanal ,el cual los datos ingresa el usuario
def calcular_promedio_semanal():
    temperaturas = [] #Aqui en esta lista se almacena las temperaturas ingresadaspor el usuario
    for dia in range(1, 8):# Este bucle itera 7 veces , el cual son los 7 dias de la semana
        temperatura = float(input(f"Ingrese la temperatura del día {dia}: "))#Se solicita al usuario igresar la temperatura actual
        temperaturas.append(temperatura)#En esta linea de codigo se agrega cada temperatura ingresada a la lista 
    if not temperaturas:# Verifica si no se han ingresado temperaturas
        return "No se han ingresado temperaturas."
    promedio = sum(temperaturas) / len(temperaturas)# Se calcula el promedio sumando todas la temperaturas y dividiendo pra el numero de temperaturas ingresadas
    print(f"El promedio semanal de temperatura es: {promedio:.2f}°C") #Se imprime el promedio semanal

calcular_promedio_semanal()#Se llama a la funcion para ejecutarla



print ("todo va bien")