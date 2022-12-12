from flask_restful import Resource, marshal_with, abort
from db_methods import DBMethods
from errors import IdNotFound
from werkzeug.exceptions import BadRequest
from additions import product_fields, model_fields, price_fields

import os

db_login = os.getenv("DB_LOGIN")
db_password = os.getenv("DB_PASSWORD")
db_ip = os.getenv("DB_IP")
db_port = os.getenv("DB_PORT")


if db_ip and db_port and db_login and db_password:
    dbm = DBMethods(f"mysql://{db_login}:{db_password}@{db_ip}:{db_port}/donuts_donut")
    print("DBMethods initialized")
else:
    print(db_ip, db_port, db_login, db_password)
    raise Exception("You need to set environment variables DB_LOGIN, DB_PASSWORD, DB_IP and DB_PORT")


class Product(Resource):
    @marshal_with(product_fields)
    def get(self, product_id):
        try:
            return dbm.get_product(product_id)
        except IdNotFound:
            raise BadRequest("Product not found")


class Products(Resource):
    @marshal_with(product_fields)
    def get(self):
        return dbm.get_products()


class Model(Resource):
    @marshal_with(model_fields)
    def get(self, product_id):
        try:
            return dbm.get_model(product_id)
        except IdNotFound:
            raise BadRequest("Model not found")


class Price(Resource):
    @marshal_with(price_fields)
    def get(self, product_id):
        try:
            return dbm.get_price(product_id)
        except IdNotFound:
            raise BadRequest("Price not found")
