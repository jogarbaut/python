from flask import render_template, redirect, request
from flask_app import app
from flask_app.models.survey import Survey

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/create/survey', methods=['POST'])
def create_survey():
    if Survey.is_valid(request.form):
        print("Survey is valid")
        Survey.save(request.form)
        return redirect('/results')
    return redirect('/')

@app.route('/results')
def results():
    return render_template('success.html', survey = Survey.get_last_survey())