"""
Module category service. Handler logic.
"""
from werkzeug.exceptions import NotFound
from app.api.model import db, Category
from app.core import validate

def get_all_category():
    return list(Category.query.all())


def create_category(args):
    new_category = Category()
    for key, value in args.items():
        if hasattr(new_category, key) and value is not None:
            validated_value = validate(key, value)
            setattr(new_category, key, validated_value)
    db.session.add(new_category)
    db.session.commit()
    return new_category


def get_category(id):
    result = Category.query.get(id)
    if not result:
        raise NotFound("Category not found!")
    else:
        return result

def update_category(id, args):
    result = get_category(id)
    for key, value in args.items():
        if hasattr(result, key) and value is not None:
            validated_value = validate(key, value)
            setattr(result, key, validated_value)

    db.session.commit()
    return result
    

