from flask_app import app
from flask_app.models.user import User
from flask import render_template, request, redirect, session
from flask_bcrypt import Bcrypt

@app.route('/process', methods=["POST"])
def process_form():
    if request.form['action'] == 'register':
        if not User.validate_registration(request.form):
            return redirect('/')
        pw_hash = bcrypt.generate_password_hash(request.form['password'])
        print(pw_hash)
        data = {
            'fname': request.form['fname'],
            'lname': request.form['lname'],
            'email': request.form['email'],
            'password': pw_hash
        }
        id = User.save(data)
        session['uuid'] = id
        return redirect('/success')
    elif request.form['action'] == 'login':
        if not User.validate_login(request.form):
            return redirect('/')
        user = User.get_one_by_email(request.form)
        session['uuid'] = user.id
        return redirect('/success')

@app.route('/logout')
def logout():
    del session['uuid']
    return redirect('/')