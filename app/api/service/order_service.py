"""
Module order service. Handler logic.
"""

from werkzeug.exceptions import NotFound
from sqlalchemy.exc import IntegrityError
# from flask import current_app
from flask import jsonify

from app.core import validate
from app.core.errors.errors import UnknownError
from app.api.model import db, Order
from .order_detail_service import create_order_detail, clear_order_detail

def get_all_order():
    return list(Order.query.all())


def create_order(args):
    with db.session.begin():
        new_order = Order()
        db.session.add(new_order)
        db.session.flush() # generate order id

        for key, value in args.items():
            if hasattr(new_order, key) and value is not None:
                validated_value = validate(key, value)
                setattr(new_order, key, validated_value)

            if key == "invoice":
                invoice = validate(key, value)
                create_order_detail(invoice, new_order.id)

    return new_order


def get_order(id):
    result = Order.query.get(id)
    if not result:
        raise NotFound("Order not found!")
    else:
        return result


def update_order(id, args):
    with db.session.begin():
        result = get_order(id)
        for key, value in args.items():
            if hasattr(result, key) and value is not None:
                validated_value = validate(key, value)
                setattr(result, key, validated_value)

            if key == "invoice":
                invoice = validate(key, value)
                clear_order_detail(id)
                create_order_detail(invoice, id)

    return result


def delete_order(id):
    try:
        with db.session.begin():
            order = get_order(id)
            db.session.delete(order)

    except IntegrityError as e: # TBD: causes
        # current_app.logger.exception(e.code)
        raise UnknownError()
    else:
        return jsonify({'info': f'Order {id} deleted!'})
 