import json
from productoo import Producto
from inventario_n import Inventario
def menu():
    inventario = Inventario()
    while True:
        print("\n---------Menú Inventario-------------")
        print("1. Agregar producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar producto por nombre")
        print("5. Mostrar todos los productos")
        print("6. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            id_producto = input("ID del producto: ")
            nombre = input("Nombre del producto: ")
            cantidad = int(input("Cantidad: "))
            precio = float(input("Precio: "))
            inventario.agregar_producto(Producto(id_producto, nombre, cantidad, precio))
            print("Producto agregado correctamente.")

        elif opcion == "2":
            id_producto = input("ID del producto a eliminar: ")
            inventario.eliminar_producto(id_producto)
            print("Producto eliminado correctamente.")

        elif opcion == "3":
            id_producto = input("ID del producto a actualizar: ")
            cantidad = input("Nueva cantidad: ")
            precio = input("Nuevo precio: ")
            cantidad = int(cantidad) if cantidad else None
            precio = float(precio) if precio else None
            inventario.actualizar_producto(id_producto, cantidad, precio)
            print("Producto actualizado correctamente.")

        elif opcion == "4":
            nombre = input("Nombre del producto : ")
            resultados = inventario.buscar_producto(nombre)
            print("Resultados:", resultados)

        elif opcion == "5":
            productos = inventario.mostrar_todos()
            print("Inventario:", productos)

        elif opcion == "6":
            print("Saliendo del inventario")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    menu()
