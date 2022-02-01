from flask_app import app
from flask_app.models.user import User
from flask import render_template, request, redirect, session

@app.route('/')
def default_route():
    return render_template("index.html")

@app.route('/success')
def success():
    if 'uuid' not in session:
        return redirect('/')
    acc = User.get_one_by_id(session)
    print(acc)
    return render_template("shopping_lists.html", user=acc)