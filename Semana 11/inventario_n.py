
import json
from productoo import Producto
class Inventario:
    def __init__(self):
        self.productos = {}
        self.cargar_desde_archivo()

    def agregar_producto(self, producto):
        self.productos[producto.id_producto] = producto
        self.guardar_en_archivo()

    def eliminar_producto(self, id_producto):
        if id_producto in self.productos:
            del self.productos[id_producto]
            self.guardar_en_archivo()

    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        if id_producto in self.productos:
            if cantidad is not None:
                self.productos[id_producto].actualizar_cantidad(cantidad)
            if precio is not None:
                self.productos[id_producto].actualizar_precio(precio)
            self.guardar_en_archivo()

    def buscar_producto(self, nombre):
        return [p.to_dict() for p in self.productos.values() if p.nombre.lower() == nombre.lower()]

    def mostrar_todos(self):
        return [p.to_dict() for p in self.productos.values()]

    def guardar_en_archivo(self):
        with open("inventario.json", "w") as archivo:
            json.dump([p.to_dict() for p in self.productos.values()], archivo, indent=4)

    def cargar_desde_archivo(self):
        try:
            with open("inventario.json", "r") as archivo:
                datos = json.load(archivo)
                for item in datos:
                    producto = Producto(item["ID"], item["Nombre"], item["Cantidad"], item["Precio"])
                    self.productos[producto.id_producto] = producto
        except (FileNotFoundError, json.JSONDecodeError):
            self.productos = {}
