from flask import Flask, render_template, request, redirect

app = Flask(__name__)
app.secret_key = "725578"

DATABASE = 'email_schema'