from flask import render_template, redirect, request
from flask_app import app
from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja

@app.route('/ninjas')
def ninjas():
    return render_template('ninja.html', dojos=Dojo.get_all())

@app.route('/create/ninja', methods=["POST"])
def create_ninja():
    Ninja.save(request.form)
    return redirect('/')
