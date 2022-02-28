from flask import render_template, request, redirect
from flask_app import app
from flask_app.models.email import Email

# Route to render templates
@app.route('/')
def index():
    return redirect("/email_form")

@app.route('/email_form')
def show_form():
    return render_template('email_form.html')

@app.route('/success')
def success():
    return render_template('success.html', emails=Email.get_all())

# POST Route Methods
# Create a new database entry
@app.route("/email/create", methods=["POST"])
def create_email():
    if not Email.validate_email(request.form):
        return redirect('/')
    Email.save(request.form)
    return redirect("/success")

# Delete a database entry
@app.route("/email/destroy/<int:id>")
def destroy_email(id):
    data = {
        "id": id
    }
    Email.destroy(data)
    return redirect("/")