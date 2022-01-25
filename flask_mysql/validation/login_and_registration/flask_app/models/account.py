from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import app, DATABASE
from flask import flash
import re
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 
NAME_REGEX = re.compile(r'^[a-zA-Z]{2,}$')

class Account:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM accounts;"
        results = connectToMySQL(DATABASE).query_db(query)
        accounts = []
        for account in results:
            print(account)
            accounts.append(cls(account))
        return accounts

    @classmethod
    def save(cls, data):
        query = "INSERT INTO accounts (first_name, last_name, email, password, created_at, updated_at) VALUES (%(fname)s, %(lname)s, %(email)s, %(password)s, NOW(), NOW());"
        return connectToMySQL(DATABASE).query_db(query, data)
    
    @classmethod
    def get_one_by_email(cls, data):
        query = "SELECT * FROM accounts WHERE email = %(email)s;"
        return connectToMySQL(DATABASE).query_db(query, data)
    
    @classmethod
    def get_one_by_id(cls, data):
        query = "SELECT * FROM accounts WHERE id = %(uuid)s;"
        return connectToMySQL(DATABASE).query_db(query, data)

    @staticmethod
    def validate_registration(data):
        is_valid = True
        if len(data['fname']) < 2:
            flash("First name must be at least 2 characters", "err_fname")
            is_valid = False
        elif not NAME_REGEX.match(data['fname']):
            flash("First name must consist of only letters", "err_fname")
            is_valid = False
        if len(data['lname']) < 2:
            flash("Last name must be at least 2 characters", "err_lname")
            is_valid = False
        elif not NAME_REGEX.match(data['lname']):
            flash("Last name must consist of only letters", "err_lname")
            is_valid = False
        if not EMAIL_REGEX.match(data['email']):
            flash("Email is not valid!", "err_email")
            is_valid = False
        if Account.get_one_by_email(data):
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
        acc = Account.get_one_by_email(data)
        print(acc)
        if not acc:
            flash("Invalid login credentials", "err_login_creds")
            is_valid = False
        elif not bcrypt.check_password_hash(acc[0]['password'], data['login_pass']):
            flash("Invalid login credentials", "err_login_creds")
            is_valid = False
        return is_valid

