from db_models import Models, Products, Prices
from flask_sqlalchemy import SQLAlchemy
from db_session import DataBase
from errors import IdNotFound


class DBMethods:
    def __init__(self, conn_str):
        self.db = DataBase(conn_str)

    def get_product(self, product_id):
        session = self.db.get_session()
        result = session.query(Products).filter(Products.product_id == product_id).first()
        if not result:
            raise IdNotFound
        return result

    def get_products(self):
        session = self.db.get_session()
        result = session.query(Products).all()
        return result

    def get_price(self, product_id):
        session = self.db.get_session()
        result = session.query(Prices).filter(Prices.product_id == product_id).first()
        if not result:
            raise IdNotFound
        return result

    def get_model(self, product_id):
        session = self.db.get_session()
        result = session.query(Models).filter(Models.product_id == product_id).first()
        if not result:
            raise IdNotFound
        return result
