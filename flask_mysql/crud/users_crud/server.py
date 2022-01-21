from flask import Flask, render_template, request, redirect
from user import User

app = Flask(__name__)

@app.route('/')
def index():
    all_users = User.get_all()
    return render_template("index.html", users=all_users)

@app.route('/new')
def new_user():
    return render_template("new_user.html")

@app.route('/create_user', methods=['POST'])
def create_user():
    data = {
        "fname": request.form["fname"],
        "lname": request.form["lname"],
        "email": request.form["email"]
    }
    User.save(data)
    return redirect('/')

@app.route('/show/<id>')
def show_user(id):
    pass

@app.route('/edit/<id>')
def edit_user(id):
    pass

@app.route('/edit_user', methods=['POST'])
def update_user():
    pass

@app.route('/delete/<id>')
def delete_user(id):

    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)