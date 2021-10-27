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
    get_user,
    update_user
)

api = UserSchema.api
user_doc = UserSchema.user_doc

parser = RequestParser()
parser.add_argument(name="username", location="json", required=True)
parser.add_argument(name="email", location="json", required=False)

parser_update = RequestParser()
parser_update.add_argument(name="name", location="json")
parser_update.add_argument(name="email", location="json")

@api.route("/")
class UserList(Resource):
    """ User router """

    @api.doc("List of users")
    @api.marshal_list_with(user_doc, envelope="data", skip_none=True)
    def get(self):
        return get_all_user()


    @api.doc("Create a user")
    @api.expect(parser)
    @api.marshal_with(user_doc, skip_none=True)
    def post(self):
        args = parser.parse_args(request)
        return create_user(args)


@api.route("/<int:user_id>")
class User(Resource):
    """ User router """

    @api.doc("Get a user")
    @api.marshal_with(user_doc, skip_none=True)
    def get(self, user_id):
        return get_user(user_id)

    @api.doc("Update a user")
    @api.expect(parser_update)
    @api.marshal_with(user_doc)
    def put(self, user_id):
        args = parser_update.parse_args(request)
        return update_user(user_id, args)