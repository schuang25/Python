import requests
from flask_app.config.mysqlconnection import connectToMySQL

DATABASE = 'ffxiv_shopping_schema'

item_list = requests.get("https://universalis.app/api/marketable").json()
# print(len(item_list)) length is 13279

#current start 2
for i in range(0, 133): # max 133
    item_string = ""
    lower = i * 100
    if i == 132:
        upper = 13279
    else:
        upper = (i+1) * 100
    for x in range(lower, upper):
        if x % 100 == 0:
            item_string += str(item_list[x])
        else:
            item_string += "," + str(item_list[x])

    items = requests.get(f"https://xivapi.com/item?ids={item_string}&private_key=ff6e74d0f35f4fa4bcf305128dcc51e99bb6f9d2ee524928a5ace82e6da2b293").json()

    # print(len(items['Results']))
    # print(items['Results'][0])

    for item in items['Results']:
        # print(item['ID'])
        # print(item['Name'])

        data = {
            'id': item['ID'],
            'name': item['Name']
        }
        select_query = "SELECT * FROM items WHERE id = %(id)s;"
        select = connectToMySQL(DATABASE).query_db(select_query, data)
        if not select:
            query = "INSERT INTO items (id, name, created_at, updated_at) VALUES (%(id)s, %(name)s, NOW(), NOW());"
            connectToMySQL(DATABASE).query_db(query, data)