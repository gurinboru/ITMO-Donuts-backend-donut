from flask_restful import fields


model_fields = {
    'id': fields.Integer(attribute='model_id'),
    'product_id': fields.Integer,
    'obj_path': fields.String,
    'mtl_path': fields.String,
}
price_fields = {
    'id': fields.Integer(attribute='price_id'),
    'product_id': fields.Integer,
    'price': fields.Integer,
}
product_fields = {
    'id': fields.Integer(attribute='product_id'),
    'title': fields.String,
    'short_description': fields.String,
    'energetic_value': fields.Integer,
    'weight': fields.Integer,
    'picture': fields.String,
    'price': fields.Nested(price_fields),
}
