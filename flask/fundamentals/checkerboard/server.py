from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/<w>')
@app.route('/<w>/<h>')
@app.route('/<w>/<h>/<colora>')
@app.route('/<w>/<h>/<colora>/<colorb>')
def checkerboard(w='8', h='8', colora='red', colorb='black'):
    print(w)
    print(h)
    return render_template("index.html", width=int(w), height=int(h), color1=colora, color2=colorb)

@app.route('/<path:path>')
def catch_all(path):
    return "a"

if __name__ == "__main__":
    app.run(debug=True)