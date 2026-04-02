from productos import (
    agregar_producto, 
    mostrar_productos, 
    total_productos, 
    eliminar_producto,
    cargar_productos
)
def menu():
    while True:
        print("\n----MENÚ----")
        print("1. Agregar producto")
        print("2. Ver producto")
        print("3. Ver total")
        print("4. Eliminar producto")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Nombre del producto: ")

            try: #Manejo de excepciones
                precio = float(input("Precio: "))
                agregar_producto(nombre, precio)
            except ValueError: #Alternativa por si falla
                print("Debes ingresar un número válido para el precio")

        elif opcion == "2":
            mostrar_productos()
        
        elif opcion == "3":
            print(f"Total: ${total_productos()}")
        
        elif opcion == "4":
            mostrar_productos()
            try:
                indice = int(input("Número del producto a eliminar: ")) -1 #Indices comienzan en 0
                eliminar_producto(indice)

            except ValueError:
                print("Debes ingresar un número válido") 

        elif opcion == "5":
            print ("Chao")
            break

        else:
            print("Opción inválida")

menu()

