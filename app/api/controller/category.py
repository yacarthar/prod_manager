"""
Module category controller. Handler router
"""
from flask import request
from flask_restx import Resource
from flask_restx.reqparse import RequestParser

from app.api.schema.category import CategorySchema
from app.api.service.category_service import (
    get_all_category,
    create_category,
    get_category
)

api = CategorySchema.api
category_doc = CategorySchema.category_doc

category_parser = RequestParser()
category_parser.add_argument(name="name", location="json", required=True)

@api.route("/")
class CategoryList(Resource):
    """ Category router """

    @api.doc("List of categories")
    @api.marshal_list_with(category_doc, envelope="data")
    def get(self):
        return get_all_category()


    @api.doc("Create a category")
    @api.expect(category_parser)
    @api.marshal_with(category_doc)
    def post(self):
        args = category_parser.parse_args(request)
        return create_category(args)


@api.route("/<int:category_id>")
class Category(Resource):
    """ Category router """

    @api.doc("Get a category")
    @api.marshal_with(category_doc)
    def get(self, category_id):
        return get_category(category_id)
