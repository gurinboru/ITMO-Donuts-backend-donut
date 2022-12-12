from flask import Flask
from flask_restful import Api, Resource
from resources import Product, Products, Model, Price
from static_setup import setup_static


app = Flask(__name__)
api = Api(app)

api_base_url = "/api/v1/donut/"

api.add_resource(Product, api_base_url + "product/<int:product_id>")
api.add_resource(Products, api_base_url + "products/")
api.add_resource(Model, api_base_url + "model/<int:product_id>")
api.add_resource(Price, api_base_url + "price/<int:product_id>")

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000)
    # setup_static()
