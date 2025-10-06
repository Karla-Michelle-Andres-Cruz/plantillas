from flask import Flask, render_template

app = Flask (__name__)

@app.route("/")
def index():
    arr = ["Luis", "Martin", "Rosa", "Paco", "Scott"]
    autor = "Karla Michelle Andre Cruz"
    return render_template("index.html", nombre = autor, amigos = arr)

@app.route('/plantilla1')
def p1():
    musica = ["cosa de dos", "flaco", "aunque te mueras por volver"]
    autores = ["Jose Jose", "Mon Laferte", "Bunburry"]
    return render_template("p1.html", musica = canciones, autores = auto )






if __name__ == "__main__":
    app.run(debug=True)