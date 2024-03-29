from flask import render_template, request, redirect, session, flash
from flask_app import app
from flask_app.models.user import User
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)

# Route to render templates
@app.route('/')
def index():
    return redirect('/dashboard')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/success')
def success():
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        'id': session['user_id']
    }
    return render_template('success.html', user=User.get_by_id(data))

@app.route('/register/user', methods=['POST'])
def register():
    if not User.validate_registration(request.form):
        return redirect('/')
    # Hashing password upon registration using Bcrpyt
    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email'],
        'password': pw_hash
    }
    id = User.save(data)
    session['user_id'] = id
    return redirect('/success')

@app.route('/destroy_session', methods=['POST'])
def reset_session():
    session.clear()
    print('Session Cleared')
    return redirect('/')

@app.route('/logout', methods=['POST'])
def logout():
    session.clear()
    print('Session Cleared')
    return redirect('/')

# Comparing provided password with the hash in the database using Bcrpyt
@app.route('/login', methods=['POST'])
def login():
    # Check if email provided exists in the database
    data = {'email': request.form['email']}
    user_in_db = User.get_by_email(data)
    # If user does not exist in the database
    if not user_in_db:
        flash('Invalid Email/Password', 'login')
        return redirect('/')
    if not bcrypt.check_password_hash(user_in_db.password, request.form['password']):
        flash('Invalid Email/Password', 'login')
        return redirect('/')
    session['user_id'] = user_in_db.id
    return redirect('/success')