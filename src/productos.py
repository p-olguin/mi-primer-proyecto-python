
from database import conectar

def obtener_productos():
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("SELECT id, nombre, precio FROM productos ORDER BY id ASC")
    productos = cursor.fetchall()

    conn.close()
    return productos


def agregar_producto(nombre, precio):
    if not nombre.strip(): #Verifica si campo esta vacio
        return False, "El nombre no puede estar vacio"

    if precio <= 0:
        return False, "El precio debe ser mayor que 0"
    
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO productos (nombre, precio) VALUES (?,?)",
        (nombre, precio)
    )

    conn.commit()
    conn.close()

    return True, "Producto agregado correctamente"


def eliminar_producto(id_producto):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("SELECT nombre FROM productos WHERE id = ?", (id_producto,))
    producto = cursor.fetchone()

    if producto is None:
        conn.close()
        return False, "Producto no encontrado"
    
    cursor.execute("DELETE FROM productos WHERE id = ?", (id_producto,))
    conn.commit()
    conn.close()

    return True, f"Producto eliminado: {producto['nombre']}"


def total_productos():
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("SELECT SUM(precio) AS total FROM productos")
    resultado = cursor.fetchone()

    conn.close()

    if resultado["total"] is None:
        return 0
    
    return resultado["total"]

def obtener_producto_por_id(id_producto):
    conn = conectar()
    cursor = conn.cursor()

    #Ejecuta la consulta
    cursor.execute(
        "SELECT id, nombre, precio FROM productos WHERE ID = ?", (id_producto,)
    )

    #recupera resultado de la consulta
    producto = cursor.fetchone()

    conn.close()
    return producto

def actualizar_producto(id_producto, nombre, precio):
    if not nombre.strip():
        return False, "El nombre no puede estar vacio"
    if precio <= 0:
        return False, "El precio debe ser mayor que 0"
    
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute(
        "UPDATE productos SET nombre = ?, precio = ? WHERE id = ?", 
        (nombre, precio, id_producto,)
    )

    conn.commit()
    conn.close()

    return True, "Producto actualizado correctamente"





