from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import app, DATABASE

class Item:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']

    @classmethod
    def get_item_by_id(self, data):
        query = "SELECT * FROM items WHERE id = %(id)s;"
        results = connectToMySQL(DATABASE).query_db(query, data)
        if results:
            return self(results[0])
        else:
            return False

    @classmethod
    def get_item_by_exact_name(self, data):
        query = "SELECT * FROM items WHERE name = %(name)s;"
        results = connectToMySQL(DATABASE).query_db(query, data)
        if results:
            return self(results[0])
        else:
            return False
    
    @classmethod
    def get_items_by_partial_name(self, data):
        query = "SELECT * FROM items WHERE name LIKE CONCAT(\"%\", %(name)s, \"%\");"
        results = connectToMySQL(DATABASE).query_db(query, data)
        items = []
        if results:
            for result in results:
                items.append(self(result))
        return items
