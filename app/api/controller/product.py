"""
Module product controller. Handler router
"""
from flask import request
from flask_restx import Resource
from flask_restx.reqparse import RequestParser

from app.api.schema.product import ProductSchema
from app.api.service.product_service import (
    get_all_product,
    create_product,
    get_product,
    update_product
)

api = ProductSchema.api
product_doc = ProductSchema.product_doc

parser = RequestParser()
parser.add_argument(name="name", location="json", required=True)
parser.add_argument(name="price", location="json", required=True)
parser.add_argument(name="category_id", location="json", required=True)

parser_update = RequestParser()
parser_update.add_argument(name="name", location="json")
parser_update.add_argument(name="price", location="json")
parser_update.add_argument(name="category_id", location="json")


@api.route("/")
class productList(Resource):
    """ Products router """

    @api.doc("List of products")
    @api.marshal_list_with(product_doc, envelope="data")
    def get(self):
        return get_all_product()


    @api.doc("Create a product")
    @api.expect(parser)
    @api.marshal_with(product_doc)
    def post(self):
        args = parser.parse_args(request)
        return create_product(args)


@api.route("/<int:produc_id>")
class product(Resource):
    """ Product router """

    @api.doc("Get a product")
    @api.marshal_with(product_doc)
    def get(self, produc_id):
        return get_product(produc_id)

    @api.doc("Update a product")
    @api.expect(parser_update)
    @api.marshal_with(product_doc)
    def put(self, produc_id):
        args = parser_update.parse_args(request)
        return update_product(produc_id, args)