from flask_app import app
from flask_app.controllers.validate import Validate
from flask import Flask, render_template, request, redirect, flash, session

@app.route('/')
def generate_form():
    return render_template("index.html")

@app.route('/submit', methods=['POST'])
def process_form():
    print(request.form)
    if not Validate.validate(request.form):
        return redirect('/')
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comments'] = request.form['comments']
    return redirect("/result")

@app.route('/result')
def show_completed_form():
    return render_template('show.html')

@app.route('/clear')
def clear_session():
    session.clear()
    return redirect('/')

@app.route('/<path:path>')
def catch_all(path):
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)