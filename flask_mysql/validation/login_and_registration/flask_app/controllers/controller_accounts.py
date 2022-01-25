from flask_app import app
from flask_app.models.account import Account
from flask import render_template, request, redirect, session
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)

@app.route('/process', methods=["POST"])
def process_form():
    if request.form['action'] == 'register':
        if not Account.validate_registration(request.form):
            return redirect('/')
        pw_hash = bcrypt.generate_password_hash(request.form['password'])
        print(pw_hash)
        data = {
            'fname': request.form['fname'],
            'lname': request.form['lname'],
            'email': request.form['email'],
            'password': pw_hash
        }
        id = Account.save(data)
        session['uuid'] = id
        return redirect('/success')
    elif request.form['action'] == 'login':
        if not Account.validate_login(request.form):
            return redirect('/')
        user = Account.get_one_by_email(request.form)
        session['uuid'] = user[0]['id']
        return redirect('/success')

@app.route('/logout')
def logout():
    del session['uuid']
    return redirect('/')