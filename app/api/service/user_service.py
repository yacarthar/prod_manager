"""
Module user service. Handler logic.
"""
from werkzeug.exceptions import NotFound
from app.api.model import db, User


def get_all_user():
    return list(User.query.all())


def create_user(args):
    new_user = User()
    for key, value in args.items():
        if hasattr(new_user, key) and value is not None:
            validated_value = validate(key, value)
            setattr(new_user, key, validated_value)
    
    db.session.add(new_user)
    db.session.commit()
    return new_user


def get_user(id):
    result = User.query.get(id)
    if not result:
        raise NotFound("User not found!")
    else:
        return result

def update_user(id, args):
    result = get_user(id)
    for key, value in args.items():
        if hasattr(result, key) and value is not None:
            validated_value = validate(key, value)
            setattr(result, key, validated_value)

    db.session.commit()
    return result
