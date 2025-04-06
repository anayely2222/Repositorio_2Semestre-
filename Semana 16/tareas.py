#Tareas con atajos
import tkinter as tk
from tkinter import messagebox  # Para mostrar mensajes de alerta

# Clase principal de la aplicación
class TaskManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title(" ------- GESTOR DE LISTA DE TAREAS -------")  # Título de la ventana
        self.root.geometry("600x600")        # Tamaño de la ventana

        # Campo de entrada para escribir tareas nuevas
        self.task_entry = tk.Entry(root, font=("Arial", 12))
        self.task_entry.pack(pady=12, padx=12, fill=tk.X)
        self.task_entry.focus()  
        # Lista donde se mostrarán las tareas
        self.task_listbox = tk.Listbox(root, font=("Arial", 12), selectmode=tk.SINGLE)
        self.task_listbox.pack(pady=12, padx=12, fill=tk.BOTH, expand=True)

        # Organizar los botones
        button_frame = tk.Frame(root)
        button_frame.pack(pady=5)

        # Botón para añadir tareas
        add_button = tk.Button(button_frame, text=" ** Añadir Tarea ** ", command=self.add_task)
        add_button.grid(row=0, column=0, padx=5)

        # Botón para marcar tareas como completadas
        complete_button = tk.Button(button_frame, text=" ** Marcar tarea Completada ** ", command=self.complete_task)
        complete_button.grid(row=0, column=1, padx=5)

        # Botón para eliminar tareas
        delete_button = tk.Button(button_frame, text=" ** Eliminar Tarea ** ", command=self.delete_task)
        delete_button.grid(row=0, column=2, padx=5)

        # Atajos de teclado
        self.root.bind('<Return>', lambda event: self.add_task())      # Enter para añadir
        self.root.bind('<c>', lambda event: self.complete_task())      # 'c' para completar
        self.root.bind('<C>', lambda event: self.complete_task())      # 'C' para completar
        self.root.bind('<d>', lambda event: self.delete_task())        # 'd' para eliminar
        self.root.bind('<D>', lambda event: self.delete_task())        # 'D' para eliminar
        self.root.bind('<Delete>', lambda event: self.delete_task())   # Tecla Delete para eliminar
        self.root.bind('<Escape>', lambda event: root.quit())          # Escape para salir

        # Diccionario que guarda el estado de cada tarea 
        self.completed_tasks = {}

    # Método para añadir una nueva tarea
    def add_task(self):
        task = self.task_entry.get().strip()  # Obtener texto del campo
        if task:
            self.task_listbox.insert(tk.END, task)  # Añadir a la lista
            self.completed_tasks[task] = False       # Registrar como tarea pendiente
            self.task_entry.delete(0, tk.END)        # Limpiar el campo de entrada
        else:
            messagebox.showwarning(" Campo vacío ", " ** Por favor, escribe una tarea. ** ")

    # Método para marcar una tarea como completada
    def complete_task(self):
        try:
            index = self.task_listbox.curselection()[0]   # Obtener índice de tarea seleccionada
            task = self.task_listbox.get(index)           # Obtener texto de la tarea
            if not self.completed_tasks.get(task, False): # Verifica si ya está completada
                self.completed_tasks[task] = True
                self.task_listbox.delete(index)           # Eliminar la tarea original
                self.task_listbox.insert(index, f"[✔] {task}")  # Insertar versión completada
                self.task_listbox.itemconfig(index, fg="gray", font=("Arial", 12, "overstrike"))  # Cambiar estilo
            else:
                messagebox.showinfo("Ya completada", "Esta tarea ya está completada.")
        except IndexError:
            messagebox.showinfo("Selecciona una tarea", " Tiene que seleccionar una tarea para marcarla como completada.")

    # Método para eliminar una tarea
    def delete_task(self):
        try:
            index = self.task_listbox.curselection()[0]  # Obtener índice de tarea seleccionada
            task = self.task_listbox.get(index)          # Obtener texto de la tarea
            self.task_listbox.delete(index)              # Eliminar de la lista
            self.completed_tasks.pop(task.replace("[✔] ", ""), None)  # Eliminar del diccionario (quita etiqueta "[✔]")
        except IndexError:
            messagebox.showinfo("Selecciona una tarea", " Tiene que seleccionar una tarea para eliminarla.")

# Iniciar la aplicación
if __name__ == "__main__":
    root = tk.Tk()               # Crea la ventana principal
    app = TaskManagerApp(root)  # Crea la instancia de la app
    root.mainloop()             # Iniciar el bucle principal de Tkinter
