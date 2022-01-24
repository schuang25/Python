from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask import flash
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

class Email:
    def __init__(self, data):
        self.id = data['id']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM emails;"
        results = connectToMySQL(DATABASE).query_db(query)
        emails = []
        for email in results:
            print(email)
            emails.append(cls(email))
        return emails

    @classmethod
    def save(cls, data):
        query = "INSERT INTO emails (email, created_at, updated_at) VALUES (%(email)s, NOW(), NOW());"
        return connectToMySQL(DATABASE).query_db(query, data)
    
    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM emails where email = %(email)s;"
        return connectToMySQL(DATABASE).query_db(query, data)
    
    @staticmethod
    def validate(data):
        is_valid = True
        if not EMAIL_REGEX.match(data['email']):
            flash("Email is not valid!")
            is_valid = False
        return is_valid