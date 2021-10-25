"""
Module user schema. Define response api schema
"""
from flask_restx import Namespace, fields


class UserSchema:
    api = Namespace("User", description="User related operations")
    user_doc = api.model(
        "user",
        {
            "user_id": fields.Integer(required=True, attribute="id"),
            "user_name": fields.String(required=True, attribute="username"),
            "user_email": fields.String(required=False, attribute="email")
        }
    )
