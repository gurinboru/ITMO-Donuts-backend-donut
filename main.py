from flask import Flask
from flask_restful import Api
from resources import Product, Products, Model, Price


app = Flask(__name__)
api = Api(app)

api_base_url = "/api/v1/donut/"

api.add_resource(Product, api_base_url + "product/<int:product_id>")
api.add_resource(Products, api_base_url + "products/")
api.add_resource(Model, api_base_url + "model/<int:product_id>")
api.add_resource(Price, api_base_url + "price/<int:product_id>")

if __name__ == "__main__":
    app.run()
