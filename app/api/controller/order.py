"""
Module order controller. Handler router
"""
from flask import request
from flask_restx import Resource
from flask_restx.reqparse import RequestParser

from app.api.schema.order import OrderSchema

from app.api.service.order_service import get_all_order, create_order, get_order, delete_order
from app.api.service.order_detail_service import get_order_detail

api = OrderSchema.api
order_doc = OrderSchema.order_doc
order_detail_doc = OrderSchema.order_detail_doc

order_parser = RequestParser()
order_parser.add_argument(name="user_id", type=int, location="json", required=True)
order_parser.add_argument(name="invoice", type=str, location="json", required=True)

@api.route("/")
class OrderList(Resource):
    """ Order router """

    @api.doc("List of orders")
    @api.marshal_list_with(order_doc, envelope="data")
    def get(self):
        return get_all_order()


    @api.doc("Create a order")
    @api.expect(order_parser)
    @api.marshal_with(order_doc)
    def post(self):
        args = order_parser.parse_args(request)
        user_id, invoice_str = args.get('user_id'), args.get('invoice')
        new_order = create_order(user_id, invoice_str)
        return new_order


@api.route("/<int:order_id>")
class Order(Resource):
    """ Order router """

    @api.doc("Get a order")
    @api.marshal_with(order_doc)
    def get(self, order_id):
        return get_order(order_id)


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