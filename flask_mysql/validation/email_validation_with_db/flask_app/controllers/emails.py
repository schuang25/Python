from flask_app import app
from flask_app.models.email import Email
from flask import Flask, render_template, request, redirect, flash, session

@app.route('/')
def default_route():
    return render_template("index.html")

@app.route('/submit', methods=["POST"])
def verify_email():
    data = {
        "email": request.form['email']
    }
    if not Email.validate(data):
        return redirect('/')
    if Email.get_one(data):
        flash("Email already exists")
        return redirect('/')
    Email.save(data)
    return redirect('/success')

@app.route('/success')
def success():
    emails_record = Email.get_all()
    return render_template("success.html", emails=emails_record)