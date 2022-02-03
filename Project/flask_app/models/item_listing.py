from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import app, DATABASE
import requests

class ItemListing:
    def __init__(self, data):
        self.id = data['id']
        self.unit_price = data['unit_price']
        self.quantity = data['quantity']
        self.world = data['world']

    @classmethod
    def get_listings(cls, data):
        listing_request = requests.get(f"https://universalis.app/api/{data['dc']}/{data['id']}?listings=10").json()
        listings = []
        for listing in listing_request['listings']:
            data = {
                'id': listing_request['itemID'],
                'unit_price': listing['pricePerUnit'],
                'quantity': listing['quantity'],
                'world': listing['worldName']
            }
            listings.append(cls(data))
        return listings
