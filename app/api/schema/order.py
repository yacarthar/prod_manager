"""
Module order schema. Define response api schema
"""
from flask_restx import Namespace, fields


class OrderSchema:
    api = Namespace("Order", description="Order related operations")
    order_doc = api.model(
        "order",
        {
            "order_id": fields.Integer(required=True, attribute="id"),
            "order_date": fields.DateTime(dt_format='rfc822', required=True, attribute="date"),
            "order_user_name": fields.String(required=True, attribute="user_name"),
            "order_cost": fields.Integer(required=True, attribute="cost"),
        }
    )

    order_detail_doc = api.model(
        "order_detail",
        {
            "order_detail_id": fields.Integer(required=True, attribute="id"),
            "order_detail_product_id": fields.Integer(required=True, attribute="product_id"),
            "order_detail_product_name": fields.String(required=True, attribute="product_name"),
            "order_detail_amount": fields.Integer(required=True, attribute="amount"),
            "order_id": fields.Integer(required=True, attribute="order_id"),
        }
    )
