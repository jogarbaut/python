from flask_app.config.mysqlconnection import connectToMySQL
from .ninja import Ninja

class Dojo:

    # Initialize class
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = []

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL('dojos_ninjas').query_db(query)
        dojos = []
        for i in results:
            dojos.append(cls(i))
        return dojos

    @classmethod
    def save(cls, data):
        query = "INSERT INTO dojos_ninjas.dojos (name) VALUES (%(name)s);"
        result = connectToMySQL('dojos_ninjas').query_db(query, data)
        return result

    @classmethod
    def get_one_with_ninjas(cls, data):
        query = "SELECT * FROM dojos LEFT JOIN ninjas on dojos.id = ninjas.dojo_id WHERE dojos.id=%(id)s;"
        result = connectToMySQL('dojos_ninjas').query_db(query, data)
        dojo = cls(result[0])
        for row in result:
            n = {
                'id': row['ninjas.id'],
                'first_name': row['first_name'],
                'last_name': row['last_name'],
                'age': row['age'],
                'created_at': row['ninjas.created_at'],
                'updated_at': row['ninjas.updated_at']
            }
            dojo.ninjas.append(Ninja(n))
        return dojo
