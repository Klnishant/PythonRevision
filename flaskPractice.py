from flask import Flask, render_template, request

app = Flask(__name__)

#Create a Flask application that displays "Hello, World!" on the homepage.
@app.route("/")
def hello():
    return "Hello, World!"

#Write a Flask route that takes a name parameter and returns "Hello, [name]!" as plain text.
@app.route("/hello/<name>")
def hello_name(name):
    return f"Hello, {name}!"

#Write a Flask route that takes a number parameter and returns the square of that number as plain text.
@app.route("/<int:num1>/square")
def square(num1):
    return f"The square of {num1} is {num1**2}"

#Write a Flask route that displays a simple HTML form that asks for a name and returns "Hello, [name]!" when submitted.
@app.route("/form", methods=["GET", "POST"])
def form():
    if request.method == "POST":
        name = request.form["name"]
        return f"Hello, {name}!"
    return render_template("form.html")

#Write a Flask route that displays a list of names in an HTML unordered list.
@app.route("/names")
def names():
    names = ["Alice", "Bob", "Charlie", "David"]
    return render_template("names.html", names=names)

app.run()