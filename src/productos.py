import json #Formato de texto ligero

productos = []

ARCHIVO = "productos.json"

def cargar_productos():
    global productos
    try:
        with open(ARCHIVO, "r", encoding="utf-8") as archivo:
            productos = json.load(archivo)
    except FileNotFoundError:
        producto = []
    except json.JSONDecodeError:
        producto = []

def guardar_productos():
    with open(ARCHIVO, "w", encoding="utf-8") as archivo:
        json.dump(productos, archivo, indent=4, ensure_ascii=False)

def agregar_producto(nombre, precio):
    if not nombre.strip(): #Verifica si campo esta vacio
        print("El nombre no puede estar vacio")
        return
    if precio <= 0:
        print("El precio debe ser mayor que 0")

    producto = {
        "nombre": nombre,
        "precio": precio
    }
    productos.append(producto)
    guardar_productos()
    print("Producto agregado correctamente")

def mostrar_productos():
    if not productos:
        print("No hay productos registrados")
        return
    
    for i, p in enumerate(productos, start=1):
        print(f"{i}. {p['nombre']} - ${p['precio']}")

def total_productos():
    total = 0
    for p in productos:
        total += p["precio"]

    return total

def eliminar_producto(indice):
    if indice <= 0 or indice >= len(productos):
        print("Índice inválido")
        return
    
    eliminado = productos.pop(indice)
    guardar_productos()
    print(f"Producto eliminado: {eliminado['nombre']}")
    

def buscar_producto():
    productos.sort("nombre")




