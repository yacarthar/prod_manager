"""
Module order detail service. Handler logic.
"""
import json
from werkzeug.exceptions import NotFound
from app.api.model import db, Order, OrderDetail
from app.core import validate


def create_order_detail(invoice, order_id):
    for product_id, amount in invoice.items():

        product_id = validate("product_id", product_id)
        amount = validate("amount", amount)

        detail_item = OrderDetail(
            product_id=product_id,
            amount=amount,
            order_id=order_id
        )
        db.session.add(detail_item)


def get_order_detail(id):
    order = Order.query.get(id)
    if not order:
        raise NotFound("Order not found!")
    else:
        detail = list(order.order_detail)
        return detail

def clear_order_detail(id):
    OrderDetail.query.filter_by(order_id = id). \
        delete(synchronize_session="fetch")