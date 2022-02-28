from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Survey:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.location = data['location']
        self.language = data['language']
        self.comment = data['comment']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def save(cls,data):
        query = "INSERT INTO dojos (name, location, language, comment, created_at, updated_at) VALUES (%(name)s, %(location)s, %(language)s, %(comment)s, NOW(), NOW());"
        result = connectToMySQL('dojo_survey_schema').query_db(query, data)
        return result

    @classmethod
    def get_last_survey(cls):
        query = "SELECT * FROM dojos ORDER BY dojos.id DESC LIMIT 1;"
        result = connectToMySQL('dojo_survey_schema').query_db(query)
        return Survey(result[0])

    @staticmethod
    def is_valid(survey):
        is_valid = True
        if len(survey['name']) < 3:
            is_valid = False
            flash("Name must be at least 3 characters")
        if len(survey['location']) < 1:
            is_valid = False
            flash("Must choose a Location")
        if len(survey['language']) < 1:
            is_valid = False
            flash("Must choose a favorite language")
        if len(survey['comment']) < 1:
            is_valid = False
            flash("Comments must be at least 1 character")
        return is_valid