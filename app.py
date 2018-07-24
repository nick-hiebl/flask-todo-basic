from flask import Flask, render_template, request, redirect
app = Flask(__name__)

todos = ["Milk the cows", "Track down the cows in the back paddock"]
done = []

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/pricing")
def pricing():
    return render_template("pricing.html")

def get_todo_page():
    return render_template("todos.html", todos=todos, done=done)

@app.route("/todos", methods=['GET', 'POST'])
def todos_page():
    if request.method == "POST":
        if len(request.form["new-name"]) > 0:
            todos.append(request.form["new-name"])
    return get_todo_page()

@app.route("/delete", methods=['POST'])
def delete_item():
    to_go = request.form["name"]
    try:
        todos.remove(to_go)
    except Exception as e:
        pass
    return redirect("/todos")

@app.route("/done", methods=['POST'])
def done_item():
    to_go = request.form["name"]
    try:
        todos.remove(to_go)
        done.append(to_go)
    except Exception as e:
        pass
    return redirect("/todos")

@app.route("/delete_done", methods=['POST'])
def done_delete():
    to_go = request.form["name"]
    try:
        done.remove(to_go)
    except Exception as e:
        pass
    return redirect("/todos")


if __name__ == "__main__":
    app.run(debug=True)
