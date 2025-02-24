import json
import os
from producto import Producto

class Inventario:
    ARCHIVO_INVENTARIO = "inventario.txt"

    def __init__(self):
        self.productos = []
        self.cargar_inventario()

    def cargar_inventario(self):
        """Carga los productos desde el archivo si existe."""
        if os.path.exists(self.ARCHIVO_INVENTARIO):
            try:
                with open(self.ARCHIVO_INVENTARIO, "r", encoding="utf-8") as f:
                    self.productos = [Producto(**p) for p in json.load(f)]
            except (FileNotFoundError, json.JSONDecodeError) as e:
                print(f"Error al cargar el inventario: {e}")
                self.productos = []
        else:
            self.guardar_inventario()

    def guardar_inventario(self):
        """Guarda los productos en el archivo."""
        try:
            with open(self.ARCHIVO_INVENTARIO, "w", encoding="utf-8") as f:
                json.dump([p.to_dict() for p in self.productos], f, indent=4)
        except PermissionError:
            print("Error: No se tienen permisos para escribir en el archivo de inventario.")

    def agregar_producto(self, id_producto, nombre, cantidad, precio):
        """Agrega un producto si el ID no existe y actualiza el archivo."""
        if any(p.get_id() == id_producto for p in self.productos):
            print("Error: Ya existe un producto con este ID.")
            return
        nuevo_producto = Producto(id_producto, nombre, cantidad, precio)
        self.productos.append(nuevo_producto)
        self.guardar_inventario()
        print("Producto agregado exitosamente.")

    def eliminar_producto(self, id_producto):
        """Elimina un producto por ID y actualiza el archivo."""
        self.productos = [p for p in self.productos if p.get_id() != id_producto]
        self.guardar_inventario()
        print("Producto eliminado (si existía).")

    def actualizar_producto(self, id_producto, nueva_cantidad=None, nuevo_precio=None):
        """Actualiza cantidad o precio de un producto y guarda los cambios."""
        for producto in self.productos:
            if producto.get_id() == id_producto:
                if nueva_cantidad is not None:
                    producto.set_cantidad(nueva_cantidad)
                if nuevo_precio is not None:
                    producto.set_precio(nuevo_precio)
                self.guardar_inventario()
                print("Producto actualizado.")
                return
        print("Producto no encontrado.")

    def buscar_por_nombre(self, nombre):
        """Busca productos por nombre y los muestra."""
        encontrados = [p for p in self.productos if nombre.lower() in p.nombre.lower()]
        if encontrados:
            for producto in encontrados:
                print(producto)
        else:
            print("No se encontraron productos con ese nombre.")

    def mostrar_productos(self):
        """Muestra todos los productos en el inventario."""
        if not self.productos:
            print("El inventario está vacío.")
        else:
            for producto in self.productos:
                print(producto)

# Ejemplo de uso
def main():
    inventario = Inventario()
    while True:
        print("\n1. Agregar producto\n2. Eliminar producto\n3. Actualizar producto\n4. Buscar por nombre\n5. Mostrar inventario\n6. Salir")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            id_producto = input("ID: ")
            nombre = input("Nombre: ")
            cantidad = int(input("Cantidad: "))
            precio = float(input("Precio: "))
            inventario.agregar_producto(id_producto, nombre, cantidad, precio)
        elif opcion == "2":
            id_producto = input("ID del producto a eliminar: ")
            inventario.eliminar_producto(id_producto)
        elif opcion == "3":
            id_producto = input("ID del producto a actualizar: ")
            nueva_cantidad = input("Nueva cantidad (deje en blanco para no cambiar): ")
            nuevo_precio = input("Nuevo precio (deje en blanco para no cambiar): ")
            inventario.actualizar_producto(id_producto, int(nueva_cantidad) if nueva_cantidad else None, float(nuevo_precio) if nuevo_precio else None)
        elif opcion == "4":
            nombre = input("Nombre del producto a buscar: ")
            inventario.buscar_por_nombre(nombre)
        elif opcion == "5":
            inventario.mostrar_productos()
        elif opcion == "6":
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida, intente nuevamente.")

if __name__ == "__main__":
    main()
