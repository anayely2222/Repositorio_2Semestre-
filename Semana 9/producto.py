#Clase Producto
class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):#Inicializa un producto con ID, nombre, cantidad y precio.
    
        self.id_producto = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio
#Representación en cadena del producto.
    def __str__(self):
        return f"ID: {self.id_producto} | Nombre: {self.nombre} | Cantidad: {self.cantidad} | Precio: ${self.precio:.2f}"

 # Métodos Getters y Setters
    def get_id(self):
        return self.id_producto

    def set_nombre(self, nuevo_nombre):
        self.nombre = nuevo_nombre

    def set_cantidad(self, nueva_cantidad):
        self.cantidad = nueva_cantidad

    def set_precio(self, nuevo_precio):
        self.precio = nuevo_precio
