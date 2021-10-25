
# Product-Manager Installation & Manual Guide

<!-- TABLE OF CONTENTS -->
<!-- <details> -->
  <!-- <summary>Table of Contents</summary> -->
## Table of Contents
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li>
        <a href="#features--examples">Features & Examples</a>
        <ul>
            <li><a href="#category">Category</a></li>
            <li><a href="#product">Product</a></li>
            <li><a href="#user">User</a></li>
            <li><a href="#order">Order</a></li>
        </ul>
    </li>
    <li>
        <a href="#roadmap">Roadmap</a>
        <ul>
            <li><a href="#working-in-progress">Working in progress</a></li>
        </ul>
    </li>
  </ol>
<!-- </details> -->

## About The Project
This is a backend API that provide operations to manage business's products.
Objects under administration are products, categories, orders, users.

### Built With
* [Python 3.8.7](https://www.python.org/downloads/release/python-387/)
* [Flask SQLAlchemy 2.5.1](https://flask-sqlalchemy.palletsprojects.com/en/2.x/)
* [Flask RestX](https://flask-restx.readthedocs.io/en/latest/)
* [psycopg2](https://www.psycopg.org/docs/)


## Getting Started
### Prerequisites
- Python > 3.5
- Python package manager: [pip](https://pypi.org/)
- Python [virtualenv](https://pypi.org/project/virtualenv/)

### Installation
1. Clone the repo:
- `git clone https://github.com/yacarthar/prod_manager.git`
- `cd prod_manager`
2. Create virtual environment (Windows/Linux):
- `virtualenv env`
- `env\Scripts\activate` (Windows) or `source venv/bin/activate` (Linux)
- `pip install -r requirements.txt`
3. Setup environment variables:
- Update your Database URI and other variables in file `.env`
4. Run application:
- `python manage.py`
- Local server:  http://127.0.0.1:5000/api/v1/
5. Create sample Database record (Optional):
- Use SQL command in file `sql_sample.sql` to create your sample data (postgresql syntax)


## Usage
You can browse API by one of following methods:
- Swagger UI for API test: http://127.0.0.1:5000/api/v1/
- Postman import config file: http://127.0.0.1:5000/api/v1/swagger.json

### Features & Examples
#### Category
- Create a category by name:
`POST /category/ {"name": "hardware"}`
- Get list of all categories:
`GET /category/`
- Get one category by id:
`GET /category/4`

#### Product
- Create a product by product's name, price & category id:

`POST /product/ {"name": "Sony Bravia 4K","price": 3800, "category_id": 10}`

- Get a list of all products:
`GET  /product/`
- Get one product by id:
`GET /product/12`

#### User
- Create a user by user's name & email:

`POST /user/ {"name": "Tyler Durden ", "email": "tyler.d@gmail.com"}`

- Get a list of all users:
`GET  /user/`
- Get one user by id:
`GET /user/4`

#### Order
- Create an order by order's user & invoice:

> invoice is a list of order's products with its price
> format: json.dumps(Dict of {"product_id": amount})
> examples: order of 4 *adidas* (Product 11) and 2 *samsung phone* (Product 8) should have invoice string like "{\"11\": 4, \"8\": 2}"

`POST /order/ {"user_id": 4, "invoice": "{\"11\": 4, \"8\": 2}"}`


- Get a list of all orders:
`GET  /order/`
- Get an order by id:
`GET /order/30`
- Get order detail (product & price in an order) by id:

`/order/30/detail`

- Delete order:
> If a order has been deleted (from order table), its detail records will also be deleted (from order_detail table
`DELETE /order/30`

## Roadmap
### Working in progress:
- validate parameter for update operations

- more CRUD:
    - add update operation
    - search object by name, category...
    - delete operation: catch more exception
- Pagination
- Logging
- Authentication
- Authorization





<!-- 
## Installation
### Prerequisite
- Python >= 3.7
- Python package management: pip, virtualenv

### Environment -->