from flask import Flask, render_template, request
from locust import HttpUser, task, between

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

class MyUser(HttpUser):
    wait_time = between(1, 3)

    @task
    def hello(self):
        self.client.get("/")

    @task
    def greet(self):
        self.client.get("/hello")

if __name__ == "__main__":
    app.run(debug=True)