"""
Module order service. Handler logic.
"""


from werkzeug.exceptions import NotFound
from sqlalchemy.exc import IntegrityError
from flask import current_app, jsonify

from app.core.errors.errors import UnknownError

from app.api.model import db, Order
from .order_detail_service import create_order_detail

def get_all_order():
    return list(Order.query.all())


def create_order(user_id, invoice_str):
    try:
        new_order = Order(user_id=user_id)
        # start transaction
        with db.session.begin():
            # create order object
            db.session.add(new_order)
            db.session.flush()
            # create order detail object
            order_detail = create_order_detail(invoice_str, new_order.id)
            db.session.add_all(order_detail)
            db.session.flush()

    except IntegrityError as e:
        current_app.logger.exception(e.code)
        raise UnknownError()
    else:
        return new_order

def get_order(id):
    result = Order.query.get(id)
    if not result:
        raise NotFound("Order not found!")
    else:
        return result


def delete_order(id):
    try:
        with db.session.begin():
            order = get_order(id)
            db.session.delete(order)

    except IntegrityError as e:
        current_app.logger.exception(e.code)
        raise UnknownError()
    else:
        return jsonify({'info': f'Order {id} deleted!'})
 