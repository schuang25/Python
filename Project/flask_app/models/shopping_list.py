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
        self.items = []

    @classmethod
    def get_all_for_user(cls, data):
        query = "SELECT * FROM shopping_lists LEFT JOIN shopping_list_items ON shopping_lists.id = shopping_list_items.shopping_list_id JOIN items ON shopping_list_items.item_id = items.id WHERE shopping_lists.user_id = %(uuid)s;"
        results = connectToMySQL(DATABASE).query_db(query, data)
        lists = []
        if results:
            current_list_id = results[0]['shopping_lists.id']
            current_list = cls(results[0])
            for result in results:
                print(result)
                if current_list_id != result['shopping_lists.id']:
                    lists.append(current_list)
                    current_list = cls(results)
                    current_list_id = results['shopping_lists_id']
                data = {
                    id: result['items.id'],
                    name: result['items.name']
                }
                current_list.items.append(Item(data))
            lists.append(current_list)
        return lists

    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM shopping_lists LEFT JOIN shopping_list_items ON shopping_lists.id = shopping_list_items.shopping_list_id JOIN items ON shopping_list_items.item_id = items.id WHERE shopping_lists.id = %(id)s;"
        results = connectToMySQL(DATABASE).query_db(query, data)
        if results:
            current_list = cls(results[0])
            for result in results:
                print(result)
                data = {
                    id: result['items.id'],
                    name: result['items.name']
                }
                current_list.items.append(Item(data))
            return current_list
        return False