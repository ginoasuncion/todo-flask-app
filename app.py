from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# A list to store our to-do items
todo_list = []


# Route to display the to-do list
@app.route("/")
def index():
    return render_template("index.html", todo_list=todo_list)


# Route to add a new to-do item
@app.route("/add", methods=["POST"])
def add_todo():
    todo = request.form.get("todo")
    todo_list.append(todo)
    return redirect(url_for("index"))


# Route to delete a to-do item
@app.route("/delete/<int:index>")
def delete_todo(index):
    del todo_list[index]
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)
