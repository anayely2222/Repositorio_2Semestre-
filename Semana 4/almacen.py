class Producto:#Clase que representa un producto en el almacén.
    def __init__(self, id_producto, nombre, categoria, cantidad, precio):
        self.id_producto = id_producto
        self.nombre = nombre
        self.categoria = categoria
        self.cantidad = cantidad
        self.precio = precio

    def aumentar_stock(self, cantidad):#Incrementa el stock del producto.
        self.cantidad += cantidad

    def reducir_stock(self, cantidad):#Reduce el stock si hay suficiente cantidad disponible.
        if self.cantidad >= cantidad:
            self.cantidad -= cantidad
            return True
        return False

    def __str__(self):# Representación en texto del producto.
        return f"{self.nombre} (Categoría: {self.categoria}) - ${self.precio:.2f} - Stock: {self.cantidad}"


class Almacen:#Clase que representa un almacén que gestiona productos.
    def __init__(self, nombre):
        self.nombre = nombre
        self.inventario = {}

    def agregar_producto(self, producto):#Agrega un nuevo producto al inventario.
        if producto.id_producto in self.inventario:
            return f"El producto {producto.nombre} ya existe en el inventario."
        self.inventario[producto.id_producto] = producto
        return f"Producto {producto.nombre} agregado al inventario."

    def listar_productos(self):#  Lista todos los productos disponibles en el almacén.

        if not self.inventario:
            return "El almacén está vacío."
        lista = f"Inventario de {self.nombre}:\n"
        for producto in self.inventario.values():
            lista += f"- {producto}\n"
        return lista

    def ingresar_stock(self, id_producto, cantidad):#Incrementa el stock de un producto existente.

        if id_producto in self.inventario:
            producto = self.inventario[id_producto]
            producto.aumentar_stock(cantidad)
            return f"Se han ingresado {cantidad} unidades al producto {producto.nombre}."
        return "Producto no encontrado en el inventario."

    def retirar_stock(self, id_producto, cantidad):#Retira stock de un producto si hay suficiente cantidad.

        if id_producto in self.inventario:
            producto = self.inventario[id_producto]
            if producto.reducir_stock(cantidad):
                return f"Se han retirado {cantidad} unidades del producto {producto.nombre}."
            return f"No hay suficiente stock para retirar {cantidad} unidades de {producto.nombre}."
        return "Producto no encontrado en el inventario."


# Ejemplo de uso
if __name__ == "__main__":
    # Crear un almacén
    almacen = Almacen("Almacén Eithan")

    # Crear productos
    producto1 = Producto(1, "Sillon", "Muebles", 60, 20.00)
    producto2 = Producto(2, "Mesa", "Muebles", 30, 45.00)
    producto3 = Producto(3, "Cocina", "Electródomestico", 10, 500.00)

    # Agregar productos al almacén
    print(almacen.agregar_producto(producto1))
    print(almacen.agregar_producto(producto2))
    print(almacen.agregar_producto(producto3))

    # Listar productos en el almacén
    print("\n" + almacen.listar_productos())

    # Ingresar stock
    print(almacen.ingresar_stock(1, 12))  # Agregar 12 sillones
    print(almacen.ingresar_stock(3, 6))   # Agregar 6 lCocinas

    # Retirar stock
    print(almacen.retirar_stock(2, 6))    # Retirar 6 mesas
    print(almacen.retirar_stock(1, 100)) # Intentar retirar más de lo disponible

    # Listar productos después de las operaciones
    print("\n" + almacen.listar_productos())
