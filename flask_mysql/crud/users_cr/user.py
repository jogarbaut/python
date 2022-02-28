# Import the function that will return an instance of a connection
from mysqlconnection import connectToMySQL

# Model the class after the user table from our database
class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    # Class methods to query our database
    # Method to retrieve all database entries
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL('users').query_db(query)
        # Create an empty list to append our instances of users
        users = []
        # Iterate over the db results and create instances of users with cls.
        for user in results:
            users.append(cls(user))
        return users
    
    # Method to retrieve one database based on an id
    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM users WHERE id = %(id)s";
        results = connectToMySQL('users').query_db(query, data)
        return cls(results[0])

    # Method to update database entry
    @classmethod
    def update(cls, data):
        query = "UPDATE users SET first_name=%(first_name)s, last_name=%(last_name)s, email=%(email)s, updated_at=NOW() WHERE id=%(id)s;"
        return connectToMySQL('users').query_db(query, data)

    # Method to save new entry into database
    @classmethod
    def save(cls, data):
        query = "INSERT INTO users (first_name, last_name, email, created_at, updated_at) VALUES (%(first_name)s,  %(last_name)s, %(email)s, NOW(), NOW());"
        return connectToMySQL('users').query_db(query, data)

    # Method to delete entry in database
    @classmethod
    def destroy(cls, data):
        query = "DELETE FROM users WHERE id=%(id)s;"
        return connectToMySQL('users').query_db(query, data)