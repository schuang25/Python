from flask_app import app, bcrypt
from flask_app.models.user import User
from flask import render_template, request, redirect, session

@app.route('/register', methods=["POST"])
def register():
    if not User.validate_registration(request.form):
        return redirect('/')
    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    print(pw_hash)
    data = {
        'username': request.form['username'],
        'email': request.form['email'],
        'password': pw_hash
    }
    id = User.save(data)
    session['uuid'] = id
    return redirect('/shopping_lists')

@app.route('/login', methods=["POST"])
def login():
    if not User.validate_login(request.form):
        return redirect('/')
    user = User.get_one_by_name(request.form)
    session['uuid'] = user.id
    return redirect('/shopping_lists')

@app.route('/logout')
def logout():
    del session['uuid']
    return redirect('/')