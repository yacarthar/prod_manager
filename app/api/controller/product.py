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
    get_product
)

api = ProductSchema.api
product_doc = ProductSchema.product_doc

product_parser = RequestParser()
product_parser.add_argument(name="name", location="json", required=True)
product_parser.add_argument(name="price", type=int, location="json", required=True)
product_parser.add_argument(name="category_id", type=int, location="json", required=True)

@api.route("/")
class productList(Resource):
    """ Products router """

    @api.doc("List of products")
    @api.marshal_list_with(product_doc, envelope="data")
    def get(self):
        return get_all_product()


    @api.doc("Create a product")
    @api.expect(product_parser)
    @api.marshal_with(product_doc)
    def post(self):
        args = product_parser.parse_args(request)
        return create_product(args)


@api.route("/<int:produc_id>")
class product(Resource):
    """ Product router """

    @api.doc("Get a product")
    @api.marshal_with(product_doc)
    def get(self, produc_id):
        return get_product(produc_id)


    # @api.doc("Get a product")
    # @api.marshal_with(product_doc)
    # def get(self, produc_id):
    #     return get_product(produc_id)