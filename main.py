from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"

@app.route("/hello", methods=["GET", "POST"])
def greet():
    if request.method == "POST":
        name = request.form.get("name")
        return render_template("greeting.html", name=name)
    else:
        return render_template("form.html")

if __name__ == "__main__":
    app.run(debug=True)
