from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Recipe:
    db_name = 'recipes'

    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.description = data['description']
        self.instructions = data['instructions']
        self.under30 = data['under30']
        self.date_made = data['date_made']
        self.user_id = data['user_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    # Class method to save data to database
    @classmethod
    def save(cls, data):
        # Change 'users' to name of table adding data to
        query = 'INSERT INTO recipes (name, description, instructions, under30, date_made, user_id) VALUES (%(name)s, %(description)s, %(instructions)s, %(under30)s,%(date_made)s, %(user_id)s);'
        return connectToMySQL(cls.db_name).query_db(query, data)

    # Class method to get all objects in database
    @classmethod
    def get_all(cls):
        query = 'SELECT * FROM recipes;'
        results = connectToMySQL(cls.db_name).query_db(query)
        all_recipes = []
        for recipe in results:
            all_recipes.append(cls(recipe))
        return all_recipes

    # Class method to retrieve a database object by id
    @classmethod
    def get_by_id(cls, data):
        query = 'SELECT * FROM recipes WHERE id=%(id)s;'
        result = connectToMySQL(cls.db_name).query_db(query, data)
        return cls(result[0])

    # Class method to update a database object
    @classmethod
    def update_recipe(cls, data):
        query = 'UPDATE recipes SET name=%(name)s, description=%(description)s, instructions=%(instructions)s, under30=%(under30)s, date_made=%(date_made)s, updated_at=NOW() WHERE id=%(id)s;'
        return connectToMySQL(cls.db_name).query_db(query, data)

    # Class method to delete a database object
    @classmethod
    def destroy(cls, data):
        query = 'DELETE FROM recipes WHERE id=%(id)s;'
        return connectToMySQL(cls.db_name).query_db(query, data)

    # Static method to validate user input
    @staticmethod
    def validate_inputs(recipe):
        is_valid = True
        if len(recipe['name']) < 3:
            flash('Recipe name must be at least 3 characters long.', 'recipe')
            is_valid = False
        if len(recipe['description']) < 3:
            flash('Recipe description must be at least 3 characters long.', 'recipe')
            is_valid = False
        if len(recipe['instructions']) < 3:
            flash('Recipe instructions must be at least 3 characters long.', 'recipe')
            is_valid = False
        if recipe['under30'] == '':
            flash('Select an option for if the recipe takes under 30 minutes to prepare.', 'recipe')
            is_valid = False
        if recipe['date_made'] == '':
            flash('Enter a date made', 'recipe')
            is_valid = False
        return is_valid