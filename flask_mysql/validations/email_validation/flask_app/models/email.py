# Import the function that will return an instance of a connection
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re

# Model the class after the user table from our database
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

class Email:
    def __init__(self, data):
        self.id = data['id']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    # Class methods to query our database
    # Method to retrieve all database entries
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM emails;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL('emails_schema').query_db(query)
        # Create an empty list to append our instances of users
        emails = []
        # Iterate over the db results and create instances of users with cls.
        for email in results:
            emails.append(cls(email))
        return emails

    # Method to save new entry into database
    @classmethod
    def save(cls, data):
        query = "INSERT INTO emails (email, created_at, updated_at) VALUES (%(email)s, NOW(), NOW());"
        return connectToMySQL('emails_schema').query_db(query, data)

    # Method to delete entry in database
    @classmethod
    def destroy(cls, data):
        query = "DELETE FROM emails WHERE id=%(id)s;"
        return connectToMySQL('emails_schema').query_db(query, data)

    # Static method to validate an entered email address
    @staticmethod
    def validate_email(email):
        is_valid = True
        if len(email['email']) < 3:
            flash('Email must be at least 3 characters')
            is_valid = False
        if not EMAIL_REGEX.match(email['email']):
            flash('Invalid email address')
            is_valid=False
        return is_valid