from flask import Flask, render_template

app = Flask (__name__)

@app.route("/")
def index():
    arr = ["Luis", "Martin", "Rosa", "Paco", "Scott"]
    autor = "Karla Michelle Andre Cruz"
    return render_template("index.html", nombre = autor, amigos = arr)






if __name__ == "__main__":
    app.run(debug=True)