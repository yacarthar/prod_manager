"""
Module user controller. Handler router
"""
from flask import request
from flask_restx import Resource
from flask_restx.reqparse import RequestParser

from app.api.schema.user import UserSchema
from app.api.service.user_service import (
    get_all_user,
    create_user,
    get_user
)

api = UserSchema.api
user_doc = UserSchema.user_doc

user_parser = RequestParser()
user_parser.add_argument(name="name", location="json", required=True)
user_parser.add_argument(name="email", location="json", required=False)

@api.route("/")
class UserList(Resource):
    """ User router """

    @api.doc("List of users")
    @api.marshal_list_with(user_doc, envelope="data", skip_none=True)
    def get(self):
        return get_all_user()


    @api.doc("Create a user")
    @api.expect(user_parser)
    @api.marshal_with(user_doc, skip_none=True)
    def post(self):
        args = user_parser.parse_args(request)
        return create_user(args)


@api.route("/<int:user_id>")
class User(Resource):
    """ User router """

    @api.doc("Get a user")
    @api.marshal_with(user_doc, skip_none=True)
    def get(self, user_id):
        return get_user(user_id)
