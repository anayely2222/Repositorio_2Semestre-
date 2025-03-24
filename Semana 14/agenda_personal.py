import tkinter as tk
import datetime 
from tkinter import ttk, messagebox
from tkcalendar import DateEntry

def agregar_evento():# Función para poder agregar un evento a la lista
    fecha = entry_fecha.get()
    hora = entry_hora.get()
    descripcion = entry_descripcion.get()
    
    if fecha and hora and descripcion: # Se verifica que los campos no estén vacíos antes de agregar el evento
        tree.insert('', 'end', values=(fecha, hora, descripcion))
        entry_fecha.set_date(datetime.date.today())
        entry_hora.delete(0, tk.END)
        entry_descripcion.delete(0, tk.END)
    else:
        messagebox.showwarning("** Advertencia **", " Todos los campos son obligatorios ")  # Se muestra una advertencia si falta algún dato

# Función para eliminar un evento seleccionado
def eliminar_evento():
    seleccionado = tree.selection()
    if seleccionado:
        if messagebox.askyesno("Confirmación", "¿Seguro que deseas eliminar el evento seleccionado?"):
            tree.delete(seleccionado)
    else:
        messagebox.showwarning("** Advertencia **", "Selecciona un evento para eliminar")# Advertencia si no se selecciona ningún evento

# Función para confirmar la salida de la aplicación
def confirmar_salida():
    if messagebox.askyesno(" Salir ", "¿Seguro que deseas salir de la agenda?"):
        root.quit()

# Configuración de la ventana principal
root = tk.Tk()
root.title(" ** AGENDA PERSONAL **")  # Título de la ventana
root.geometry("800x600")  # Tamaño de la ventana

# Frame para la entrada de datos
frame_entrada = tk.Frame(root)
frame_entrada.pack(pady=10)# Se agrega espacio alrededor del frame

# Etiquetas para identificar los campos
tk.Label(frame_entrada, text="Fecha:").grid(row=0, column=0)
tk.Label(frame_entrada, text="Hora:").grid(row=1, column=0)
tk.Label(frame_entrada, text="Descripción:").grid(row=2, column=0)

# Campo de selección de fecha con DateEntry
entry_fecha = DateEntry(frame_entrada, width=12, background='darkblue', foreground='white', borderwidth=2)
entry_fecha.grid(row=0, column=1)

# Campos de entrada para hora y descripción
tk.Label(frame_entrada, text="Formato HH:MM").grid(row=1, column=2)
entry_hora = tk.Entry(frame_entrada)
entry_hora.grid(row=1, column=1)

entry_descripcion = tk.Entry(frame_entrada)
entry_descripcion.grid(row=2, column=1)

# Botón para agregar evento
tk.Button(frame_entrada, text="  Agregar Evento  ", command=agregar_evento).grid(row=3, column=0, columnspan=2, pady=5)

# Frame para la lista de eventos
frame_lista = tk.Frame(root)
frame_lista.pack()

# Treeview para mostrar la lista de eventos
tree = ttk.Treeview(frame_lista, columns=("Fecha", "Hora", "Descripción"), show='headings')
tree.heading("Fecha", text="Fecha")
tree.heading("Hora", text="Hora")
tree.heading("Descripción", text="Descripción")
tree.pack()

# Botón para eliminar evento seleccionado
tk.Button(root, text="Eliminar Evento Seleccionado", command=eliminar_evento).pack(pady=5)

# Botón para salir de la aplicación con confirmación
tk.Button(root, text=" ---- Salir ---- ", command=confirmar_salida).pack(pady=5)

# Ejecutar el bucle principal de la aplicación
root.mainloop()
