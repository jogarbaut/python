from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'top secret key'


@app.route('/')
def index():
    if 'count' in session:
        session['count'] += 1
    else:
        session['count'] = 1
    return render_template('index.html', count=session['count'])

@app.route('/add_two', methods=['POST'])
def add_two():
    session['count'] += 1
    return redirect('/')

@app.route('/destroy_session', methods=['POST'])
def reset_session():
    session.clear()
    return redirect('/')


if __name__=="__main__":
    app.run(debug=True, port=8000)