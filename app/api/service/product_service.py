"""
Module product service. Handler logic.
"""
from werkzeug.exceptions import NotFound
from app.api.model import db, Product


def get_all_product():
    return list(Product.query.all())


def create_product(args):
    new_product = Product(
        name = args.get('name'),
        price = args.get('price'),
        category_id = args.get('category_id')
    )
    db.session.add(new_product)
    db.session.commit()
    return new_product


def get_product(id):
    result = Product.query.get(id)
    if not result:
        raise NotFound("Product not found!")
    else:
        return result