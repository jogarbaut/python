from flask import render_template, request, redirect, session, flash
from flask_app import app
from flask_app.models.user import User
from flask_app.models.recipe import Recipe

@app.route('/new/recipe')
def new_recipe():
    print('Got to new recipe')
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        'id': session['user_id']
    }
    return render_template('new_recipe.html')

@app.route('/recipe/<int:recipe_id>')
def view_recipe(recipe_id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        'id': recipe_id
    }
    user_data = {
        'id': session['user_id']
    }
    return render_template('show_recipe.html', recipe=Recipe.get_by_id(data), user=User.get_by_id(user_data))

@app.route('/edit/recipe/<int:recipe_id>')
def edit_recipe(recipe_id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        'id': recipe_id
    }
    user_data = {
        'id': session['user_id']
    }
    return render_template('edit_recipe.html',edit=Recipe.get_by_id(data),user=User.get_by_id(user_data))

@app.route('/destroy/recipe/<int:recipe_id>')
def destroy_recipe(recipe_id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        'id': recipe_id
    }
    Recipe.destroy(data)
    return redirect('/dashboard')

@app.route('/create/recipe', methods=['POST'])
def create_recipe():
    if 'user_id' not in session:
        return redirect('/logout')
    if not Recipe.validate_inputs(request.form):
        return redirect('/new/recipe')
    # Hashing password upon registration using Bcrpyt
    data = {
        'name': request.form['name'],
        'description': request.form['description'],
        'instructions': request.form['instructions'],
        'under30': request.form['under30'],
        'date_made': request.form['date_made'],
        'user_id': session['user_id'],
    }
    Recipe.save(data)
    return redirect('/dashboard')

@app.route('/update/recipe', methods=['POST'])
def update_recipe():
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        'id': request.form['id'],
        'name': request.form['name'],
        'description': request.form['description'],
        'instructions': request.form['instructions'],
        'under30': request.form['under30'],
        'date_made': request.form['date_made'],
    }
    Recipe.update_recipe(data)
    return redirect('/dashboard')