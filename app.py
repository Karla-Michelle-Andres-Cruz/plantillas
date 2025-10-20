from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask (__name__)

app.config['SECRET_KEY']='TIAMIOSSOTT12'

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/inicio")
def inicio():
    return render_template("inicio.html")

@app.route("/animales")
def an():
    return render_template("animales.html")

@app.route("/autos")
def aut():
    return render_template("autos.html")

@app.route("/7Maravillas")
def Mara():
    return render_template("maravillas.html")

@app.route("/acercade")
def acerca():
    return render_template("acerca.html")

@app.route("/registro")
def registro():
    return render_template("registro.html")

@app.route("/inicioSesión")
def sesión():
    return render_template("inicioSe.html")

@app.route("/registrame", methods=["GET", "POST"])
def registrame():
    if request.method == "POST":
        nombre = request.form["nombre"]
        apellido = request.form["apellido"]
        genero = request.form["genero"]
        email = request.form["email"]
        contraseña = request.form["contraseña"]
        conf_contraseña = request.form["confirmaContraseña"]

        emails_registrados = ["test@example.com", "juan@correo.com"]

        if email in emails_registrados:
            flash("Este correo ya está registrado", "error")
            return render_template("registro.html")
        
        if contraseña != conf_contraseña:
            flash("La contraseña no coincide", "error")
            return render_template("registro.html")

        flash(f"¡Registro exitoso para el usuario: {nombre} {apellido}", "success")
        return render_template("inicio.html")

    return render_template("registro.html")





if __name__ == "__main__":
    app.run(debug=True)