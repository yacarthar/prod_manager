"""
Module API Create Blueprint API
"""

from flask import Blueprint
from flask_restx import Api

from app.api.controller.product import api as product_ns
from app.api.controller.category import api as category_ns
from app.api.controller.user import api as user_ns
from app.api.controller.order import api as order_ns
from app.config import is_local_env

api_v1_blueprint = Blueprint("api_v1_blueprint", __name__, url_prefix="/api/v1")


api_v1 = Api(
    api_v1_blueprint,
    title="Product Manager",
    version="1.0",
    description="Product Manager",
    ui=is_local_env,
)

api_v1.add_namespace(product_ns, path="/product")
api_v1.add_namespace(category_ns, path="/category")
api_v1.add_namespace(user_ns, path="/user")
api_v1.add_namespace(order_ns, path="/order")
