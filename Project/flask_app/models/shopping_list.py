from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import app, DATABASE
from flask_app.models.item import Item

class ShoppingList:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.data_center = data['data_center']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']
        self.items = []

    @classmethod
    def add_item(cls, data):
        success = True
        query = "SELECT * FROM items WHERE id = %(item_id)s;"
        results = connectToMySQL(DATABASE).query_db(query, data)
        if results:
            add_query = "INSERT INTO shopping_list_items (shopping_list_id, item_id, created_at, updated_at) VALUES (%(id)s, %(item_id)s, NOW(), NOW());"
            connectToMySQL(DATABASE).query_db(add_query, data)
            update_query = "UPDATE shopping_lists SET updated_at = NOW() WHERE id = %(id)s;"
            connectToMySQL(DATABASE).query_db(update_query, data)
        else:
            flash ("Item ID not found", "err_invalid_id")
            success = False
        return success
    
    @classmethod
    def delete_item(cls, data):
        query = "DELETE FROM shopping_list_items WHERE shopping_list_id = %(list_id)s AND item_id = %(item_id)s;"
        connectToMySQL(DATABASE).query_db(query, data)
        update_query = "UPDATE shopping_lists SET updated_at = NOW() WHERE id = %(list_id)s;"
        connectToMySQL(DATABASE).query_db(update_query, data)

    @classmethod
    def get_all_for_user(cls, data):
        query = "SELECT * FROM shopping_lists LEFT JOIN shopping_list_items ON shopping_lists.id = shopping_list_items.shopping_list_id LEFT JOIN items ON shopping_list_items.item_id = items.id WHERE shopping_lists.user_id = %(uuid)s;"
        results = connectToMySQL(DATABASE).query_db(query, data)
        lists = []
        if results:
            print(results[0])
            current_list_id = results[0]['id']
            current_list = cls(results[0])
            for result in results:
                print(result)
                if current_list_id != result['id']:
                    lists.append(current_list)
                    current_list = cls(result)
                    current_list_id = result['id']
                if result['items.id'] != None:
                    data = {
                        'id': result['items.id'],
                        'name': result['items.name']
                    }
                    current_list.items.append(Item(data))
            lists.append(current_list)
        return lists

    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM shopping_lists LEFT JOIN shopping_list_items ON shopping_lists.id = shopping_list_items.shopping_list_id LEFT JOIN items ON shopping_list_items.item_id = items.id WHERE shopping_lists.id = %(id)s;"
        results = connectToMySQL(DATABASE).query_db(query, data)
        if results:
            current_list = cls(results[0])
            for result in results:
                print(result)
                if result['items.id'] != None:
                    data = {
                        'id': result['items.id'],
                        'name': result['items.name']
                    }
                    current_list.items.append(Item(data))
            return current_list
        return False
    
    @classmethod
    def save(cls, data):
        query = "INSERT INTO shopping_lists (name, data_center, created_at, updated_at, user_id) VALUES (%(name)s, %(dc)s, NOW(), NOW(), %(user_id)s);"
        return connectToMySQL(DATABASE).query_db(query, data)