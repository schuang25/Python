from flask_app import app
from flask_app.models.user import User
from flask import render_template, request, redirect, session

@app.route('/')
def default_route():
    if 'uuid' in session:
        return redirect('/shopping_lists')
    return render_template("index.html")