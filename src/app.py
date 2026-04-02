from flask import Flask, render_template, request, redirect, url_for
from productos import obtener_productos, agregar_producto, eliminar_producto, total_productos
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

@app.route("/eliminar/ <int:id_producto>")
def eliminar(id_producto):
    eliminar_producto(id_producto)
    return redirect(url_for("ver_productos"))

if __name__ == "__main__":
    app.run(debug=True)


