from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = "725578"

@app.route('/')
def counter():
    if 'counter' in session:
        session['counter'] += 1
    else:
        session['counter'] = 1
    return render_template("index.html")

@app.route('/destroy_session')
def destroy_session():
    session.clear()
    return redirect('/')

# Extra functions to come later

@app.route('/<path:path>')
def catch_all(path):
    pass

if __name__ == "__main__":
    app.run(debug=True)