from flask import render_template, request, redirect
from flask_app import app
from flask_app.models.user import User

# Route to render templates
@app.route("/")
def index():
    return redirect("/users")

# Render template to show all users
@app.route("/users")
def users():
    users = User.get_all()
    return render_template("users.html", all_users = users)

# Render template to add a new user
@app.route("/users/new")
def new():
    return render_template("new_user.html")

# Render template to show new page with user details
@app.route("/users/show/<int:id>")
def show(id):
    data = {
        "id": id
    }
    return render_template("show_user.html", user = User.get_one(data))

# Render template to show new page to edit user
@app.route("/users/edit/<int:id>")
def edit(id):
    data = {
        "id":id
    }
    return render_template("edit_user.html", user = User.get_one(data))


# POST Route Methods
# Create a new database entry
@app.route("/users/create", methods=["POST"])
def create_user():
    User.save(request.form)
    return redirect("/")

# Update a database entry
@app.route("/users/update", methods=["POST"])
def update_user():
    User.update(request.form)
    return redirect("/")

# Delete a database entry
@app.route("/users/destroy/<int:id>")
def destroy_user(id):
    data = {
        "id": id
    }
    User.destroy(data)
    return redirect("/")