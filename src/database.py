import sqlite3

DATABASE = "src/productos.db"

def conectar(): #Abre base de datos
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row #Permite acceder a columnas por nombre
    return conn

def crear_tabla(): #Crea la tabla si no existe
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS productos (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   nombre TEXT NOT NULL,
                   precio REAL NOT NULL
                   )
    """)

    conn.commit()
    conn.close()