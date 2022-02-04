from flask_app import app
from flask_app.models.user import User
from flask_app.models.item import Item
from flask_app.models.shopping_list import ShoppingList
from flask import render_template, request, redirect, session, flash

@app.route('/shopping_lists')
def display_lists():
    if 'uuid' not in session:
        return redirect('index.html')
    acc = User.get_one_by_id(session)
    print(acc)
    lists = ShoppingList.get_all_for_user(session)
    return render_template("shopping_lists.html", user=acc, shopping_lists=lists)

@app.route('/shopping_lists/new')
def new_list():
    if 'uuid' not in session:
        return redirect('index.html')
    acc = User.get_one_by_id(session)
    print(acc)
    return render_template("new_list.html", user=acc)

@app.route('/shopping_lists/create', methods=["POST"])
def create_list():
    if 'uuid' not in session:
        return redirect('index.html')
    data = {
        'name': request.form['name'],
        'dc': request.form['dc'],
        'user_id': session['uuid']
    }
    id = ShoppingList.save(data)
    return redirect('/shopping_lists/show/' + str(id))

@app.route('/shopping_lists/show/<int:id>')
def show_list(id):
    if 'uuid' not in session:
        return redirect('index.html')
    data = {
        'id': str(id)
    }
    acc = User.get_one_by_id(session)
    item_list = ShoppingList.get_one(data)
    if item_list.user_id != session['uuid']:
        return redirect('/shopping_lists')
    return render_template("list_display.html", user=acc, shopping_list=item_list)

@app.route('/shopping_lists/add_item/<int:id>', methods=['POST'])
def add_item_to_list(id):
    if 'uuid' not in session:
        return redirect('index.html')
    data = {
        **request.form,
        'id': str(id)
    }
    ShoppingList.add_item(data)
    return redirect('/shopping_lists/show/' + str(id))

@app.route('/shopping_lists/delete_item/<int:list_id>/<int:item_id>')
def delete_item_from_list(list_id, item_id):
    data = {
        'list_id': str(list_id),
        'item_id': str(item_id)
    }
    ShoppingList.delete_item(data)
    return redirect('/shopping_lists/show/' + str(list_id))