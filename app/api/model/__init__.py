"""database model
"""

from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=True)

    def __repr__(self):
        return f'<User {self.id}: {self.username}>'

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    price = db.Column(db.Integer, nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'),
                            nullable=True)

    @property
    def category_name(self):
        return self.category.name

    def __repr__(self):
        return f'<Product {self.id}: {self.name}>'


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    products = db.relationship('Product',
        backref=db.backref('category', lazy=True)
    )
    def __repr__(self):
        return f'<Category {self.id}: {self.name}>'


class OrderDetail(db.Model):
    __tablename__ = 'order_detail'
    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Integer, nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=True)
    order_id = db.Column(db.Integer, db.ForeignKey('order.id'), nullable=True)
    product = db.relationship('Product')

    @property
    def product_name(self):
        return self.product.name


class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    order_detail = db.relationship('OrderDetail', cascade='all, delete, delete-orphan')
    user = db.relationship('User',
    	backref=db.backref('orders', lazy=True, cascade='all, delete, delete-orphan')
    )

    @property
    def user_name(self):
        return self.user.username

    @property
    def cost(self):
        cost = 0
        for item in self.order_detail:
            price = Product.query.get(item.product_id).price
            cost += price * item.amount
        return cost
    
    def __repr__(self):
        return '<Order %r>' % self.id
