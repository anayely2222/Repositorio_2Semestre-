from producto import Producto

class clase_inventario: #Clase inventario
    def __init__(self):# Inicializa el inventario con una lista vacía de productos.
        self.productos = []

    def agregar_producto(self, id_producto, nombre, cantidad, precio):# Se añade un nuevo producto si el ID no existe.
        if any(p.get_id() == id_producto for p in self.productos):
            print("Error: Ya existe un producto con este ID.")
            return
        nuevo_producto = Producto(id_producto, nombre, cantidad, precio)
        self.productos.append(nuevo_producto)
        print("Producto agregado exitosamente.")
#Elimina un producto por su ID.
    def eliminar_producto(self, id_producto):
        self.productos = [p for p in self.productos if p.get_id() != id_producto]
        print("Producto eliminado (si existía).")
#Actualiza cantidad o precio de un producto por su ID.
    def actualizar_producto(self, id_producto, nueva_cantidad=None, nuevo_precio=None):
        for producto in self.productos:
            if producto.get_id() == id_producto:
                if nueva_cantidad is not None:
                    producto.set_cantidad(nueva_cantidad)
                if nuevo_precio is not None:
                    producto.set_precio(nuevo_precio)
                print("Producto actualizado.")
                return
        print("Producto no encontrado.")
#Busca productos por nombre 
    def buscar_por_nombre(self, nombre):

        encontrados = [p for p in self.productos if nombre.lower() in p.nombre.lower()]
        if encontrados:
            for producto in encontrados:
                print(producto)
        else:
            print(" No se encontraron productos con ese nombre.")
#Muestra todos los productos en el inventario.
    def mostrar_productos(self):
        if not self.productos:
            print("El inventario está vacío.")
        else:
            for producto in self.productos:
                print(producto)
