"""
Core Module: Utilities functions
"""
from typing import Dict
import json
import re
from werkzeug.exceptions import BadRequest

from app.api.model import Category, Order, User
from app.constants import USERNAME_RULE, NAME_RULE, INVOICE_RULE

def validate(attribute, value):
    if attribute in ['price']:
        # if type(value) is not int:
            # raise BadRequest("Price must be integer number!") #TBD: db float
        value = float(value)
        if value <= 0:
            raise BadRequest("Price must be positive number!")

    if attribute in ['name']:
        pattern = r'^(?![_])(?!.*[_]{2})[\w\s.-]{,50}(?<![-._])$'
        if re.match(pattern, value) is None:
            raise BadRequest(f"Name must follow: \n {NAME_RULE}")

    if attribute in ['username']:
        pattern = r'^(?![-._])(?!.*[_.-]{2})[\w.-]{6,30}(?<![-._])$'
        if re.match(pattern, value) is None:
            raise BadRequest(f"Username must follow: \n {USERNAME_RULE}")

    if attribute in ['email']:
        pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        if re.match(pattern, value) is None:
            raise BadRequest(f"Invalid Email")

    if "id" in attribute:
        try:
            value = int(value)
        except ValueError:
            raise BadRequest("ID must be integer number!")
        if value <= 0:
            raise BadRequest("ID must be positive number!")
        else:
            if attribute == "category_id":
                if Category.query.get(value) is None:
                    raise BadRequest("Category ID not exist")

            if attribute == "order_id":
                if Order.query.get(value) is None:
                    raise BadRequest("Order ID not exist")

            if attribute == "user_id":
                if User.query.get(value) is None:
                    raise BadRequest("User ID not exist")

    if attribute in ["amount"]:
        try:
            value = int(value)
        except ValueError:
            raise BadRequest("Amount must be integer number!")
        if value <= 0:
            raise BadRequest("Amount must be positive number!")

    if attribute in ["invoice"]:
        try:
            value: Dict[str, int] = json.loads(value,
                object_pairs_hook=add_up_duplicates
            )
        except json.JSONDecodeError:
            raise BadRequest(f"Invalid Invoice format: {INVOICE_RULE}")

    return value


def add_up_duplicates(ordered_pairs):
    """Add up amount if duplicate product."""
    d = {}
    for k, v in ordered_pairs:
        if k in d:
           # raise ValueError(f"duplicate product id: {k}")
            d[k] += v
        else:
           d[k] = v
    return d