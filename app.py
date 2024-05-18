from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime
import math

app = Flask(__name__)

# A list to store our to-do items as dictionaries with 'task', 'timestamp', 'completed', and 'end_timestamp'
todo_list = []
completed_todo_list = []
ITEMS_PER_PAGE = 5


# Route to display the to-do list
@app.route("/")
@app.route("/page/<int:active_page>/completed/<int:completed_page>")
def index(active_page=1, completed_page=1):
    active_start_index = (active_page - 1) * ITEMS_PER_PAGE
    active_end_index = active_start_index + ITEMS_PER_PAGE
    completed_start_index = (completed_page - 1) * ITEMS_PER_PAGE
    completed_end_index = completed_start_index + ITEMS_PER_PAGE

    total_active_pages = math.ceil(len(todo_list) / ITEMS_PER_PAGE)
    total_completed_pages = math.ceil(len(completed_todo_list) / ITEMS_PER_PAGE)

    return render_template(
        "index.html",
        todo_list=todo_list[active_start_index:active_end_index],
        completed_todo_list=completed_todo_list[
            completed_start_index:completed_end_index
        ],
        active_page=active_page,
        completed_page=completed_page,
        total_active_pages=total_active_pages,
        total_completed_pages=total_completed_pages,
    )


# Route to add a new to-do item
@app.route("/add", methods=["POST"])
def add_todo():
    todo = request.form.get("todo")
    if todo:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        todo_list.append(
            {
                "task": todo,
                "timestamp": timestamp,
                "completed": False,
                "end_timestamp": None,
            }
        )
    return redirect(url_for("index"))


# Route to delete a to-do item
@app.route("/delete/<int:index>")
def delete_todo(index):
    if 0 <= index < len(todo_list):
        del todo_list[index]
    return redirect(url_for("index"))


# Route to delete a completed to-do item
@app.route("/delete_completed/<int:index>")
def delete_completed(index):
    if 0 <= index < len(completed_todo_list):
        del completed_todo_list[index]
    return redirect(url_for("index"))


# Route to mark a to-do item as complete
@app.route("/complete/<int:index>")
def complete_todo(index):
    if 0 <= index < len(todo_list):
        todo = todo_list.pop(index)
        todo["completed"] = True
        todo["end_timestamp"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        completed_todo_list.append(todo)
    return redirect(url_for("index"))


# Route to mark a completed to-do item as incomplete
@app.route("/uncomplete/<int:index>")
def uncomplete_todo(index):
    if 0 <= index < len(completed_todo_list):
        todo = completed_todo_list.pop(index)
        todo["completed"] = False
        todo["end_timestamp"] = None
        todo_list.append(todo)
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)
