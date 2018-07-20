from flask import Flask, render_template, request
app = Flask(__name__)

todos = ["Milk the cows", "Track down the cows in the back paddock"]

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/pricing")
def pricing():
    return render_template("pricing.html")

@app.route("/todos", methods=['GET', 'POST'])
def todos_page():
    if request.method == "POST":
        if len(request.form["new-name"]) > 0:
            todos.append(request.form["new-name"])
        else:
            return render_template("404.html", title="Input error",
                content="""UWU you must've made a fucky wucky.
Your todo items should have a couple letters in them at least right?""")
    return render_template("todos.html", todos=todos)

@app.route("/delete", methods=['POST'])
def delete_item():
    to_go = request.form["name"]
    todos.remove(to_go)
    return render_template("todos.html", todos=todos)

if __name__ == "__main__":
    app.run(debug=True)
