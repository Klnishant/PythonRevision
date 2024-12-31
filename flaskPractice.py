from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"

@app.route("/hello/<name>")
def hello_name(name):
    return f"Hello, {name}!"

@app.route("/<int:num1>/square")
def square(num1):
    return f"The square of {num1} is {num1**2}"


app.run()