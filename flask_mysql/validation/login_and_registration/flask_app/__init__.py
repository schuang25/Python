from flask import Flask, render_template, request, redirect

app = Flask(__name__)
app.secret_key = "725578"

DATABASE = 'accounts_schema'

from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)