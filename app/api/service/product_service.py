"""
Module product service. Handler logic.
"""
import json

from werkzeug.exceptions import NotFound
from app.api.model import db, Product
from app.core import validate

def get_all_product():
    return list(Product.query.all())


def create_product(args):
    new_product = Product()
    for key, value in args.items():
        if hasattr(new_product, key) and value is not None:
            validated_value = validate(key, value)
            setattr(new_product, key, validated_value)
            
    db.session.add(new_product)
    db.session.commit()
    return new_product


def get_product(id):
    result = Product.query.get(id)
    if not result:
        raise NotFound("Product not found!")
    else:
        return result

def update_product(id, args):
    result = get_product(id)
    for key, value in args.items():
        if hasattr(result, key) and value is not None:
            validated_value = validate(key, value)
            setattr(result, key, validated_value)

    db.session.commit()
    return result
