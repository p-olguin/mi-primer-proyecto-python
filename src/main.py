from productos import agregar_producto, mostrar_productos, total_productos

def menu():
    while True:
        print("\n----MENÚ----")
        print("1. Agregar producto")
        print("2. Ver producto")
        print("3. Ver total")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Nombre del producto: ")
            precio = float(input("Precio: "))
            agregar_producto(nombre, precio)

        elif opcion == "2":
            mostrar_productos()
        
        elif opcion == "3":
            print(f"Total: ${total_productos()}")

        elif opcion == "4":
            print ("Chao")
        
            break

        else:
            print("Opción inválida")

menu()

