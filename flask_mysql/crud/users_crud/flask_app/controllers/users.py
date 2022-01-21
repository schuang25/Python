from flask_app import app
from flask import Flask, render_template, request, redirect
from flask_app.models.user import User

@app.route('/')
def index():
    all_users = User.get_all()
    return render_template("index.html", users=all_users)

@app.route('/new')
def new_user():
    return render_template("new_user.html")

@app.route('/create_user', methods=['POST'])
def create_user():
    data = {
        "fname": request.form["fname"],
        "lname": request.form["lname"],
        "email": request.form["email"]
    }
    id = User.save(data)
    return redirect('/show/' + str(id))

@app.route('/show/<id>')
def show_user(id):
    id_dict = {"id": id}
    user_record = User.get_one(id_dict)
    return render_template("show_one.html", user=user_record)

@app.route('/edit/<id>')
def edit_user(id):
    id_dict = {"id": id}
    user_record = User.get_one(id_dict)
    return render_template("edit_user.html", user=user_record)

@app.route('/edit_user/<id>', methods=['POST'])
def update_user(id):
    data = {
        "id": id,
        "fname": request.form["fname"],
        "lname": request.form["lname"],
        "email": request.form["email"]
    }
    User.update(data)
    return redirect('/show/' + str(id))

@app.route('/delete/<id>')
def delete_user(id):
    id_dict = {"id": id}
    User.delete(id_dict)
    return redirect('/')