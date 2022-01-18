from flask import Flask, render_template, request, redirect, session
import random

app = Flask(__name__)
app.secret_key = "725578"

@app.route('/')
def guessing_game():
    res = -1
    if 'number' not in session:
        session['number'] = random.randint(1, 100)
    if 'guess_num' in session:
        if session['guess_num'] == -1:
            res = -2
        else:
            if session['guess_num'] == session['number']:
                res = 0
            elif session['guess_num'] < session['number']:
                res = 1
            else:
                res = 2
            if 'guess_count' in session:
                session['guess_count'] += 1
            else:
                session['guess_count'] = 1
    return render_template("index.html", result=res)

@app.route('/guess', methods=['POST'])
def process_guess():
    if request.form['guess'].isdigit():
        session['guess_num'] = int(request.form['guess'])
        if session['guess_num'] > 100 or session['guess_num'] < 1:
            session['guess_num'] = -1
    else: 
        session['guess_num'] = -1
    return redirect('/')

@app.route('/reset', methods=['POST'])
def reset_game():
    session.clear()
    return redirect('/')

@app.route('/<path:path>')
def catch_all(path):
    pass

if __name__ == "__main__":
    app.run(debug=True)