import sqlalchemy as sa
from sqlalchemy import orm
from db_session import SqlAlchemyBase


class Models(SqlAlchemyBase):
    __tablename__ = 'models'

    model_id = sa.Column(sa.Integer, primary_key=True, nullable=False)
    product_id = sa.Column(sa.Integer, sa.ForeignKey('products.product_id'))
    obj_path = sa.Column(sa.String(100), nullable=False)
    mtl_path = sa.Column(sa.String(100), nullable=False)

    def __repr__(self):
        return f'<Model> {self.model_id} {self.product_id} {self.obj_path} {self.mtl_path}'


class Products(SqlAlchemyBase):
    __tablename__ = 'products'

    product_id = sa.Column(sa.Integer, primary_key=True, nullable=False)
    title = sa.Column(sa.String(30), nullable=False)
    short_description = sa.Column(sa.String(100))
    energetic_value = sa.Column(sa.String(100))
    weight = sa.Column(sa.Integer)
    picture = sa.Column(sa.String(100))
    price = orm.relationship('Prices', backref='Products')

    def __repr__(self):
        return f"Products(product_id={self.product_id}, " \
               f"title={self.title}, " \
               f"short_description={self.short_description}, " \
               f"energetic_value={self.energetic_value}, " \
               f"weight={self.weight}, " \
               f"picture={bool(self.picture)}, " \
               f"price={self.price})"


class Prices(SqlAlchemyBase):
    __tablename__ = 'prices'

    price_id = sa.Column(sa.Integer, primary_key=True, nullable=False)
    product_id = sa.Column(sa.Integer, sa.ForeignKey('products.product_id'))
    price = sa.Column(sa.Integer, nullable=False)

    def __repr__(self):
        return f"Prices(price_id={self.price_id}, " \
               f"product_id={self.product_id}, " \
               f"price={self.price}, "
