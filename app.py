from flask import Flask, render_template

app = Flask (__name__)

@app.route("/")
def index():
    return render_template("index.html")

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



if __name__ == "__main__":
    app.run(debug=True)