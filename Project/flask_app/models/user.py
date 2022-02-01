from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import app, DATABASE
from flask import flash
import re
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 
USERNAME_REGEX = re.compile(r'^[a-zA-Z][a-zA-Z0-9]{1,19}$')

class User:
    def __init__(self, data):
        self.id = data['id']
        self.username = data['username']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL(DATABASE).query_db(query)
        users = []
        for user in results:
            print(user)
            users.append(cls(user))
        return users

    @classmethod
    def save(cls, data):
        query = "INSERT INTO users (username, email, password, created_at, updated_at) VALUES (%(username)s, %(email)s, %(password)s, NOW(), NOW());"
        return connectToMySQL(DATABASE).query_db(query, data)
    
    @classmethod
    def get_one_by_email(cls, data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        return cls(connectToMySQL(DATABASE).query_db(query, data)[0])
    
    @classmethod
    def get_one_by_id(cls, data):
        query = "SELECT * FROM users WHERE id = %(uuid)s;"
        return cls(connectToMySQL(DATABASE).query_db(query, data)[0])

    @staticmethod
    def validate_registration(data):
        is_valid = True
        if len(data['username']) < 2:
            flash("Username must be at least 2 characters", "err_username")
            is_valid = False
        elif not USERNAME_REGEX.match(data['username']):
            flash("Username must consist of only alphanumeric characters, starting with a letter", "err_username")
            is_valid = False
        if not EMAIL_REGEX.match(data['email']):
            flash("Email is not valid!", "err_email")
            is_valid = False
        if User.get_one_by_email(data):
            flash("Email already exists in database", "err_email")
            is_valid = False
        if len(data['password']) < 8:
            flash("Password must be at least 8 characters", "err_pass")
            is_valid = False
        if data['pass_confirm'] != data['password']:
            flash("Passwords do not match", "err_pass")
            is_valid = False
        return is_valid

    @staticmethod
    def validate_login(data):
        is_valid = True
        acc = User.get_one_by_email(data)
        print(acc)
        if not acc:
            flash("Invalid login credentials", "err_login_creds")
            is_valid = False
        elif not bcrypt.check_password_hash(acc.password, data['login_pass']):
            flash("Invalid login credentials", "err_login_creds")
            is_valid = False
        return is_valid

