from flask import Flask, render_template, request, redirect

app = Flask(__name__)
app.secret_key = "725578"

DATABASE = 'dojos_and_ninjas_schema'