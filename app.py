from flask import Flask, render_template, request, redirect, url_for, flash, session
from datetime import datetime
app = Flask (__name__)

app.config['SECRET_KEY']='TIAMIOSSOTT12'

usuariosRegist = {
    'admin@correo.com':{
        'contraseña': 'Admin123',
        'nombre': 'Administrador',
        'fecha_nacimiento': '1990-01-01'
    }
}

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
    dias = list(range(1, 32))
    meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio","Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
    año_actual = datetime.now().year
    años = list(range(año_actual, 1905, -1))
    return render_template("registro.html", dias=dias, meses=meses, años=años)

@app.route("/inicio_sesion")
def sesion():
    if session.get('logueado'):
        return redirect(url_for("inicio"))
    return render_template("inicioSe.html")

@app.route("/validalogin", methods=['POST'])
def validaLogin():
    if request.method == "POST":
        email = request.form.get('email', '').strip()
        contraseña = request.form.get('contraseña', '')
        
        if not email or not contraseña:
            flash('Por favor ingresa email y contraseña', 'error')
            return redirect(url_for('sesion'))
        
        if email in usuariosRegist:
            usuario = usuariosRegist[email]
            if usuario['contraseña'] == contraseña:
                session['usuario_email'] = email
                session['usuario'] = usuario['nombre']
                session['logueado'] = True
                flash(f"Bienvenido {usuario['nombre']}", "success")
                return redirect(url_for('inicio'))
            else:
                flash('Contraseña incorrecta', 'error')
        else:
            flash('Usuario no encontrado', 'error')
        
        return redirect(url_for('sesion'))


@app.route("/registrame", methods=["GET", "POST"])
def registrame():
    error = None
    if request.method == "POST":
        nombre = request.form["nombre"]
        apellido = request.form["apellido"]
        genero = request.form["genero"]
        email = request.form["email"]
        contraseña = request.form["contraseña"]
        conf_contraseña = request.form["confirmaContraseña"]



        if contraseña != conf_contraseña:
            flash("La contraseña no coincide", "error")
            return render_template("registro.html")
        
        if error != None: flash(error) 
        return render_template("registro.html") 
    else: 
        flash(f"¡Registro exitoso para el usuario: {nombre, apellido}") 
        return render_template ("inicio.html") 
    






if __name__ == "__main__":
    app.run(debug=True)