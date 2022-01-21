from flask_app import app
from flask import Flask, render_template, request, redirect
from flask_app.models.ninja import Ninja
from flask_app.models.dojo import Dojo

@app.route('/')
def root_redirect():
    return redirect('/dojos')

@app.route('/dojos')
def show_dojos():
    all_dojos = Dojo.get_all()
    return render_template("index.html", dojos = all_dojos)

@app.route('/dojos/<id>')
def show_dojo(id):
    data = {
        "id": id
    }
    dojo_record = Dojo.get_one(data)
    return render_template("dojo.html", dojo = dojo_record)

@app.route('/ninja')
def new_ninja():
    all_dojos = Dojo.get_all()
    return render_template("new_ninja.html", dojos = all_dojos)

@app.route('/create_ninja', methods=["POST"])
def create_ninja():
    data = {
        "fname": request.form['fname'],
        "lname": request.form['lname'],
        "age": request.form['age'],
        "dojo_id": request.form['location']
    }
    Ninja.save(data)
    return redirect('/dojos/' + request.form['location'])

@app.route('/create_dojo', methods=["POST"])
def create_dojo():
    data = {
        "name": request.form['name']
    }
    Dojo.save(data)
    return redirect('/dojos')