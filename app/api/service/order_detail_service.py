"""
Module order detail service. Handler logic.
"""
import json
from werkzeug.exceptions import NotFound
from app.api.model import Order, OrderDetail


def create_order_detail(invoice_str, order_id):
    invoice = json.loads(invoice_str)
    detail_items = list(
        OrderDetail(product_id=str(key), amount=value, order_id=order_id)
        for (key, value) in invoice.items()
    )
    return detail_items


def get_order_detail(id):
    order = Order.query.get(id)
    if not order:
        raise NotFound("Order not found!")
    else:
        detail = list(order.order_detail)
        return detail