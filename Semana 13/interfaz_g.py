import tkinter as tk # Importa la librería Tkinter para la creación de la GUI
from tkinter import messagebox # Importa messagebox para mostrar mensajes emergentes

def agregar_dato():
    #Obtiene el texto ingresado por el usuario y lo agrega a la lista si no está vacío. Muestra una advertencia si el campo está vacío.
    dato = entrada_texto.get()# Captura el texto ingresado por el usuario
    if dato:
        lista_datos.insert(tk.END, dato) # Se agrega el dato al final de la lista
        entrada_texto.delete(0, tk.END) # Se limpia el campo de entrada después de agregar el dato.
    else:
        messagebox.showwarning("Advertencia", "Ingrese un dato antes de agregar.")# Muestra una advertencia siempre y cuando el campo está vacío

def limpiar_lista():#Elimina todos los datos de la lista de datos.
    lista_datos.delete(0, tk.END)

#Se crea la ventana principal
ventana = tk.Tk()# Inicializa la ventana principal de la aplicación
ventana.title("-- Interfaz Gráfica de Usuario --")  # Título de la ventana
ventana.geometry("500x400")  # Tamaño de la ventana

# Crear y colocar los componentes de la interfaz gráfica
label = tk.Label(ventana, text="******** Ingrese un dato: ********")
label.pack(pady=5)

entrada_texto = tk.Entry(ventana, width=40)# Se crea un campo de entrada de texto con un ancho de 40 caracteres
entrada_texto.pack(pady=5)

boton_agregar = tk.Button(ventana, text="--- Agregar ---", command=agregar_dato) # Se crea un botón que ejecuta la función agregar
boton_agregar.pack(pady=5)

lista_datos = tk.Listbox(ventana, width=50, height=10) #Se crea una lista para mostrar los datos que se agrego
lista_datos.pack(pady=5)

boton_limpiar = tk.Button(ventana, text="--- Limpiar ---", command=limpiar_lista)# Crea un botón que ejecuta la función limpiar
boton_limpiar.pack(pady=5)

# Iniciar el bucle de la aplicación
ventana.mainloop()
