from flask_app import app
from flask_app.models.user import User
from flask_app.models.item import Item
from flask_app.models.item_listing import ItemListing
from flask import render_template, request, redirect, session, jsonify, flash

@app.route('/search')
def search_form():
    if 'uuid' in session:
        acc = User.get_one_by_id(session)
    else:
        acc = False
    return render_template("search.html", user=acc)

@app.route('/search/id', methods=["POST"])
def search_by_id():
    # move verification somewhere else later
    item = Item.get_item_by_id(request.form)
    if not item:
        flash("Item ID does not exist in marketable item database", "err_invalid_id")
        return redirect('/search')
    if request.form['dc'] == '':
        flash("Please select a data center to search", "err_no_dc")
        return redirect('/search')
    return redirect('/search/' + request.form['dc'] + '/' + str(item.id))

@app.route('/search/name', methods=["POST"])
def search_by_name():
    # move verification somewhere else later
    item = Item.get_item_by_exact_name(request.form)
    if not item:
        flash("Item name does not exist in marketable item database", "err_invalid_name")
        return redirect('/search')
    if request.form['dc'] == '':
        flash("Please select a data center to search", "err_no_dc")
        return redirect('/search')
    return redirect('/search/' + request.form['dc'] + '/' + str(item.id))

@app.route('/search/<string:dc>/<int:id>')
def show_item(dc, id):
    if 'uuid' in session:
        acc = User.get_one_by_id(session)
    else:
        acc = False
    data = {
        'dc': dc,
        'id': id
    }
    item_record = Item.get_item_by_id(data)
    if not item_record:
        flash("Item ID does not exist in marketable item database", "err_invalid_id")
        return redirect('/search')
    else:
        market_listings = ItemListing.get_listings(data)
        return render_template("item_details.html", user=acc, item=item_record, listings=market_listings)