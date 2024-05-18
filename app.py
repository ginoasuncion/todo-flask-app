from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime

app = Flask(__name__)

# A list to store our to-do items as dictionaries with 'task' and 'timestamp'
todo_list = []

# Route to display the to-do list
@app.route("/")
def index():
    return render_template("index.html", todo_list=todo_list)

# Route to add a new to-do item
@app.route("/add", methods=["POST"])
def add_todo():
    todo = request.form.get("todo")
    if todo:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        todo_list.append({"task": todo, "timestamp": timestamp})
    return redirect(url_for("index"))

# Route to delete a to-do item
@app.route("/delete/<int:index>")
def delete_todo(index):
    if 0 <= index < len(todo_list):
        del todo_list[index]
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)
