class Libro: # Clase que representa un libro en la biblioteca
    def __init__(self, titulo, autor, categoria, isbn):
        self.info = (autor, titulo) # Tupla que almacena autor y título de forma inmutable
        self.categoria = categoria
        self.isbn = isbn

    def __str__(self):
        return f"{self.info[1]} de {self.info[0]} (Categoría: {self.categoria}, ISBN: {self.isbn})"# Representación en cadena del libro

class Usuario:# Clase que representa un usuario de la biblioteca
    def __init__(self, nombre, user_id):
        self.nombre = nombre
        self.user_id = user_id
        self.libros_prestados = [] # Lista de libros prestados por el usuario

    def __str__(self):
        return f"Usuario: {self.nombre} (ID: {self.user_id})"     # Representación en cadena del usuario

class Biblioteca:   # Clase que gestiona la biblioteca y sus operaciones
    def __init__(self):
        self.libros_disponibles = {} # Diccionario con ISBN como clave y objeto Libro como valor
        self.usuarios_registrados = set() # Conjunto de IDs de usuarios registrados
        self.prestamos = {} # Diccionario con el historial de préstamos por usuario

    def agregar_libro(self, libro):  # Agrega un libro al catálogo de la biblioteca
        self.libros_disponibles[libro.isbn] = libro

    def eliminar_libro(self, isbn): # Elimina un libro del catálogo usando su ISBN
        self.libros_disponibles.pop(isbn, None)

    def registrar_usuario(self, usuario): # Registra un nuevo usuario en la biblioteca
        self.usuarios_registrados.add(usuario.user_id)
        self.prestamos[usuario.user_id] = []

    def eliminar_usuario(self, user_id): # Elimina un usuario si no tiene libros prestados
        if not self.prestamos[user_id]:
            self.usuarios_registrados.discard(user_id)
            self.prestamos.pop(user_id, None)

    def prestar_libro(self, user_id, isbn):# Presta un libro a un usuario si está registrado y el libro está disponible
        if user_id in self.usuarios_registrados and isbn in self.libros_disponibles:
            libro = self.libros_disponibles.pop(isbn)
            self.prestamos[user_id].append(libro)

    def devolver_libro(self, user_id, isbn): # Permite a un usuario devolver un libro a la biblioteca
        for libro in self.prestamos[user_id]:
            if libro.isbn == isbn:
                self.prestamos[user_id].remove(libro)
                self.libros_disponibles[isbn] = libro
                break

    def buscar_libro(self, criterio, valor):# Busca libros por un criterio 
        return [libro for libro in self.libros_disponibles.values() if valor.lower() in str(getattr(libro, criterio)).lower()]

    def listar_libros_prestados(self, user_id): # Devuelve la lista de libros prestados por un usuario específico
        return self.prestamos.get(user_id, [])

# Ejecución 
biblioteca = Biblioteca()
libro1 = Libro("Cien años de soledad", "Gabriel García Márquez", "Realismo Mágico", "111111111")
libro2 = Libro("Don Quijote de la Mancha", "Miguel de Cervantes", "Clásico", "222222222")
libro3 = Libro("Orgullo y prejuicio", "Jane Austen", "Romance", "333333333")
libro4 = Libro("Crimen y castigo", "Fiódor Dostoyevski", "Novela psicológica", "444444444")
usuario1 = Usuario("Anayely Quezada", "A001") #Creacion de usuario

biblioteca.registrar_usuario(usuario1)# Registro de usuario en la biblioteca
biblioteca.agregar_libro(libro1)# Agregar libros a la biblioteca
biblioteca.agregar_libro(libro2)
biblioteca.agregar_libro(libro3)
biblioteca.agregar_libro(libro4)
biblioteca.prestar_libro("A001", "111111111")# Prestar un libro al usuario

print([str(libro) for libro in biblioteca.listar_libros_prestados("A001")])# Mostrar libros prestados por el usuario
biblioteca.devolver_libro("A001", "111111111")# Devolver el libro prestado
print([str(libro) for libro in biblioteca.listar_libros_prestados("A001")])# Mostrar libros prestados nuevamente (debería estar vacío)

