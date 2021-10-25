"""
Module user service. Handler logic.
"""
from werkzeug.exceptions import NotFound
from app.api.model import db, User


def get_all_user():
    return list(User.query.all())


def create_user(args):
    new_user = User(username = args.get('name'),
        email = args.get('email')
    )
    db.session.add(new_user)
    db.session.commit()
    return new_user


def get_user(id):
    result = User.query.get(id)
    if not result:
        raise NotFound("User not found!")
    else:
        return result