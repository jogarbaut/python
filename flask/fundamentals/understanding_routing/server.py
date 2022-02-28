from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/dojo')
def dojo():
    return 'Dojo!'

@app.route('/say/<string:name>')
def say_name(name):
    return f'Hi {name.capitalize()}!'

@app.route('/repeat/<int:times>/<string:text>')
def repeat(times, text):
    statement = ''
    for i in range(0, times):
        statement += f"<p>{text}</p>"
    return statement

@app.route('/<string:other>')
def other(other):
    return 'Sorry! No response. Try again.'

if __name__=="__main__":
    app.run(debug=True, port=8000)