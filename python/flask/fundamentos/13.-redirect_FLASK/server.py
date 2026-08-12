from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/registrar", methods=["POST"])
def registrar_producto():
    nombre = request.form["nombre"]
    precio = request.form["precio"]
    categoria = request.form["categoria"]
    
    print("============================")
    print("Producto recibido")
    print(f"Nombre: {nombre}")
    print(f"Precio: {precio}")
    print(f"Categoría: {categoria}")
    print("============================")
    
    return redirect("/mostrar")

@app.route("/mostrar")
def mostrar_producto():
    return render_template("mostrar.html")

@app.route("/ayuda")
def ayuda():
    return render_template("ayuda.html")

if __name__ == "__main__":
    app.run(debug=True)