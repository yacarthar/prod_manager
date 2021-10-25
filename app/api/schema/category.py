"""
Module category schema. Define response api schema
"""
from flask_restx import Namespace, fields


class CategorySchema:
    api = Namespace("Category", description="Category related operations")
    category_doc = api.model(
        "category",
        {
            "category_id": fields.Integer(required=True, attribute="id"),
            "category_name": fields.String(required=True, attribute="name")
        }
    )
