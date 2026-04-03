from flask import Flask, render_template, request, redirect, url_for
from productos import obtener_productos, agregar_producto, eliminar_producto, total_productos, obtener_producto_por_id, actualizar_producto
from database import crear_tabla

app = Flask(__name__) #Flask crea app con name (variable que permite a flask saber donde buscar)

crear_tabla()

@app.route("/") #Cuando alguien ingrese a la ruta / muestra la funcion de abajo
def inicio():
    return render_template("index.html")


@app.route("/productos", methods=["GET", "POST"])
def ver_productos():
    mensaje = ""

    if request.method == "POST":
        nombre = request.form.get("nombre", "").strip()
        precio_texto = request.form.get("precio", "").strip()

        try:
            precio = float(precio_texto)
            exito, mensaje = agregar_producto(nombre, precio)
        except ValueError:
            mensaje = "Debes ingresar un precio válido"
        
    productos = obtener_productos()
    total = total_productos()  

    return render_template(
        "productos.html",
        productos=productos,
        total=total,
        mensaje=mensaje
    )

@app.route("/editar/<int:id_producto>", methods=["GET", "POST"])
def editar(id_producto):
    producto = obtener_producto_por_id(id_producto)

    if producto is None:
        return "Producto no encontrado", 404
    
    mensaje = ""

    if request.method == "POST":
        nombre = request.form.get("nombre", "").strip()
        precio_texto = request.form.get("precio", "").strip()

        try:
            precio = float(precio_texto)
            exito, mensaje = actualizar_producto(id_producto, nombre, precio)

            if exito:
                return redirect(url_for("ver_productos"))
        
        except ValueError:
            mensaje = "Debes ingresar un precio valido"

        producto = obtener_producto_por_id(id_producto)

    return render_template("editar_producto.html", producto=producto, mensaje=mensaje)

            
@app.route("/eliminar/ <int:id_producto>")
def eliminar(id_producto):
    eliminar_producto(id_producto)
    return redirect(url_for("ver_productos"))




if __name__ == "__main__":
    app.run(debug=True)


