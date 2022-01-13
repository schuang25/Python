from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello World!"

@app.route('/dojo')
def dojo():
    return "Dojo!"

@app.route('/say/<name>')
def greet(name):
    if (name is not None):
        return "Hi " + name.capitalize() + "!"
    else:
        return "Input error, format is \"/say/<text>\""

@app.route('/repeat/<count>/<text>')
def repeat(count, text):
    if (count.isnumeric() and text is not None):
        num = int(count)
        return (text + " ") * num
    else:
        return "Input error, format is \"/repeat/number/text\""

@app.route('/<path:path>')
def catch_all(path):
    return "Sorry! No response. Try again."

if __name__ == "__main__":
    app.run(debug=True)