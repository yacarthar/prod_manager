"""
Module category service. Handler logic.
"""
from werkzeug.exceptions import NotFound
from app.api.model import db, Category


def get_all_category():
    return list(Category.query.all())


def create_category(args):
    new_category = Category(name = args.get('name'))
    db.session.add(new_category)
    db.session.commit()
    return new_category


def get_category(id):
    result = Category.query.get(id)
    if not result:
        raise NotFound("Category not found!")
    else:
        return result