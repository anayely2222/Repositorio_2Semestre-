from inventario import clase_inventario

def mostrar_menu():
    print("-------------------- SISTEMA DE INVENTARIO------------------ ")
    print("1. Añadir Producto")
    print("2. Eliminar Producto")
    print("3. Actualizar Producto")
    print("4. Buscar producto por nombre")
    print("5. Mostrar todos los productos")
    print("6. *** Salir ***")

def main():
    inventario = clase_inventario()

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            id_producto = input("Ingrese ID único: ")
            nombre = input("Ingrese nombre del producto: ")
            cantidad = int(input("Ingrese cantidad: "))
            precio = float(input("Ingrese precio: "))
            inventario.agregar_producto(id_producto, nombre, cantidad, precio)

        elif opcion == "2":
            id_producto = input("Ingrese ID del producto que desee eliminar: ")
            inventario.eliminar_producto(id_producto)

        elif opcion == "3":
            id_producto = input("Ingrese ID del producto que desee actualizar: ")
            nueva_cantidad = input("Nueva cantidad : ")
            nuevo_precio = input("Nuevo precio : ")

            nueva_cantidad = int(nueva_cantidad) if nueva_cantidad else None
            nuevo_precio = float(nuevo_precio) if nuevo_precio else None
            inventario.actualizar_producto(id_producto, nueva_cantidad, nuevo_precio)

        elif opcion == "4":
            nombre = input("Ingrese el nombre del producto a buscar: ")
            inventario.buscar_por_nombre(nombre)

        elif opcion == "5":
            inventario.mostrar_productos()

        elif opcion == "6":
            print(" Gracias por su ingreso ............Saliendo del inventario...")
            break

        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()
