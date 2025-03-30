import tkinter as tk
from tkinter import messagebox

def agregar_tarea(event=None):# Función para agregar una nueva tarea a la lista
    tarea = entrada_tarea.get().strip()
    if tarea:
        lista_tareas.insert(tk.END, tarea)# Se agrega la tarea al final de la lista
        entrada_tarea.delete(0, tk.END)
    else:
        messagebox.showwarning("**Advertencia**", "La tarea no puede estar vacía.")# Mostrar advertencia si la tarea está vacía


def marca_completada():# Función para marcar una tarea como completada
    try:
        index = lista_tareas.curselection()[0]
        tarea = lista_tareas.get(index)
        lista_tareas.delete(index)
        lista_tareas.insert(index, f"✔ {tarea}")
    except IndexError:
        messagebox.showwarning("**Advertencia**", "Seleccione una tarea para marcar como completada.")

def eliminar_tarea(): # Función para eliminar una tarea seleccionada
    try:
        index = lista_tareas.curselection()[0]
        lista_tareas.delete(index)
    except IndexError:
        messagebox.showwarning("**Advertencia**", "Seleccione una tarea para eliminar.")

# Configuración de la ventana principal
root = tk.Tk()
root.title(" ------ Lista de Tareas ------")
root.geometry("600x500")

# Campo de entrada y botón de añadir
tk.Label(root, text=" Tarea Nueva: ").pack(pady=5)
entrada_tarea = tk.Entry(root, width=50)
entrada_tarea.pack(pady=5)
entrada_tarea.bind("<Return>", agregar_tarea)

boton_agregar = tk.Button(root, text="  - - Añadir Tarea - - ", command=agregar_tarea)# Botón para agregar tareas a la lista
boton_agregar.pack(pady=5)

# Lista de tareas actuales
lista_tareas = tk.Listbox(root, width=50, height=15)
lista_tareas.pack(pady=5)
lista_tareas.bind("<Double-Button-1>", lambda event: marca_completada())

# Botones de acción
boton_completar = tk.Button(root, text="  Marcar como Completada  ", command=marca_completada)# Botón para marcar una tarea como completada
boton_completar.pack(pady=5)

boton_eliminar = tk.Button(root, text="  Eliminar Tarea   ", command=eliminar_tarea)# Botón para eliminar una tarea seleccionada
boton_eliminar.pack(pady=5)

#  bucle principal de la aplicación
root.mainloop()
