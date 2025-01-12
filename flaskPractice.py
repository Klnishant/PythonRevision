from flask import Flask, render_template, request, jsonify

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

#Q6. Write a Flask route that displays a list of names in a table.
@app.route("/names/table")
def name_with_tables():
    names = ["Alice", "Bob", "Charlie", "David"]
    return render_template("table.html",names=names)

#Q7. Write a Flask route that displays a list of names in a dropdown menu.
@app.route("/dropdown")
def name_in_drop_down():
    names = ["Alice", "Bob", "Charlie", "David"]
    return render_template("dropdown.html",names=names)

#Q8. Write a Flask route that receives data through a POST request and returns the data in JSON format.
@app.route("/json")
def data_in_json():
    data = request.get_json()
    return jsonify(data)

app.run()