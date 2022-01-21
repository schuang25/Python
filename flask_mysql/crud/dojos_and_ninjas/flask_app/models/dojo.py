from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask_app.models import ninja

class Dojo:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = []

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL(DATABASE).query_db(query)
        dojos = []
        for dojo in results:
            print(dojo)
            dojos.append(cls(dojo))
        return dojos

    @classmethod
    def save(cls, data):
        query = "INSERT INTO dojos (name, created_at, updated_at) VALUES (%(name)s, NOW() , NOW());"
        return connectToMySQL(DATABASE).query_db(query, data)

    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM dojos JOIN ninjas ON dojos.id = ninjas.dojo_id WHERE ninjas.dojo_id = %(id)s;"
        results = connectToMySQL(DATABASE).query_db(query, data)
        if (results):
            dojo = cls(results[0])
            for row in results:
                ninja_info = {
                    "id": row['ninjas.id'],
                    "first_name": row['first_name'],
                    "last_name": row['last_name'],
                    "age": row['age'],
                    "created_at": row['ninjas.created_at'],
                    "updated_at": row['ninjas.updated_at'],
                    "dojo_id": row['dojo_id']
                }
                dojo.ninjas.append(ninja.Ninja(ninja_info))
            return dojo
        else:
            return False
