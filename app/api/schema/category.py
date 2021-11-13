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

    category_list_doc = api.model(
        "category_list",
        {
            "data": fields.List(fields.Nested(
                {
                    "category_id": fields.Integer(required=True),
                    "category_name": fields.String(required=True)
                })
            )
        }
    )
