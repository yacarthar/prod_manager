"""
Module product schema. Define response api schema
"""
from flask_restx import Namespace, fields


class ProductSchema:
    api = Namespace("Product", description="Product related operations")
    product_doc = api.model(
        "product",
        {
            "product_id": fields.Integer(required=True, attribute="id"),
            "product_name": fields.String(required=True, attribute="name"),
            "product_price": fields.Integer(required=True, attribute="price"),
            "product_category": fields.String(required=True, attribute="category_name")
        }
    )
