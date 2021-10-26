"""
Module order controller. Handler router
"""
from flask import request
from flask_restx import Resource
from flask_restx.reqparse import RequestParser

from app.api.schema.order import OrderSchema

from app.api.service.order_service import (
    get_all_order,
    create_order,
    get_order,
    update_order,
    delete_order
)
from app.api.service.order_detail_service import get_order_detail

api = OrderSchema.api
order_doc = OrderSchema.order_doc
order_detail_doc = OrderSchema.order_detail_doc

parser = RequestParser()
parser.add_argument(name="user_id", location="json", required=True)
parser.add_argument(name="invoice", location="json", required=True)

parser_update = RequestParser()
parser_update.add_argument(name="user_id", location="json")
parser_update.add_argument(name="invoice", location="json")

@api.route("/")
class OrderList(Resource):
    """ Order router """

    @api.doc("List of orders")
    @api.marshal_list_with(order_doc, envelope="data")
    def get(self):
        return get_all_order()


    @api.doc("Create a order")
    @api.expect(parser)
    @api.marshal_with(order_doc)
    def post(self):
        args = parser.parse_args(request)
        return create_order(args)


@api.route("/<int:order_id>")
class Order(Resource):
    """ Order router """

    @api.doc("Get a order")
    @api.marshal_with(order_doc)
    def get(self, order_id):
        return get_order(order_id)

    @api.doc("Update a order")
    @api.expect(parser_update)
    @api.marshal_with(order_doc)
    def put(self, order_id):
        args = parser_update.parse_args(request)
        return update_order(order_id, args)

    @api.doc("Delete a order")
    # @api.marshal_with(order_doc)
    def delete(self, order_id):
        return delete_order(order_id)


@api.route("/<int:order_id>/detail")
class OrderDetail(Resource):
    """ Order router """

    @api.doc("Get detail of a order")
    @api.marshal_with(order_detail_doc, envelope="data")
    def get(self, order_id):
        return get_order_detail(order_id)