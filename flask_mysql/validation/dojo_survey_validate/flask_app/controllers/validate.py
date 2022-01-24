from flask import flash

class Validate:
    @staticmethod
    def validate(data:dict):
        is_valid = True
        if len(data['name']) < 3:
            flash("Name must be at least 3 characters.")
            is_valid = False
        if data['location'] == '':
            flash("Must choose dojo location.")
            is_valid = False
        if data['language'] == '':
            flash("Must choose favorite language.")
            is_valid = False
        if len(data['comments']) < 1:
            flash("Must have a comment.")
            is_valid = False
        return is_valid