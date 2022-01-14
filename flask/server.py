# Flask server framework

from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)

@app.route('/<path:path>')
def catch_all(path):
    pass

if __name__ == "__main__":
    app.run(debug=True)