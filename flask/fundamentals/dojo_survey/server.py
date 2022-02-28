from flask import Flask, render_template, session, redirect, request  # Import Flask to allow us to create our app

app = Flask(__name__)    # Create a new instance of the Flask class called "app"

app.secret_key="Secret Key"

@app.route('/')          # The "@" decorator associates this route with the function immediately following
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comments'] = request.form['comments']
    return redirect('/success')

@app.route('/success')
def success():
    return render_template('success.html')

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True, port=8000)    # Run the app in debug mode.