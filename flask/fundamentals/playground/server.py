from flask import Flask, render_template

app = Flask(__name__)

@app.route('/play')
@app.route('/play/<num>')
@app.route('/play/<num>/<color>')
def draw_boxes(num="3", color="skyblue"):
    return render_template("index.html", boxes=int(num), bgcolor=color)

@app.route('/<path:path>')
def catch_all(path):
    return "a"

if __name__ == "__main__":
    app.run(debug=True)