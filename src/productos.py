productos = []

def agregar_producto(nombre, precio):
    producto = {
        "nombre": nombre,
        "precio": precio
    }
    productos.append(producto)

def mostrar_productos():
    for p in productos():
        print(f"{p['nombre']} - ${p['precio']}")

def total_productos():
    total = 0
    for p in productos:
        total += p["precio"]

    return total



