"""test view category"""

import json

from flask_restx import fields, marshal

from app.api.schema.category import CategorySchema



def test_get_category(client):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/api/v1/category/4' page is requested (GET)
    THEN check that the response is valid
    """
    res = client.get('/api/v1/category/4')
    assert res.status_code == 200
    expected = {
        "category_id": 4,
        "category_name": "clothes"
    }
    assert expected == json.loads(res.get_data(as_text=True))

def test_list_category_(client):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/api/v1/category/' page is requested (GET)
    THEN check that the response is valid
    """
    res = client.get('/api/v1/category/')
    assert res.status_code == 200

    data = json.loads(res.get_data(as_text=True))
    categories = data.get("data")
    assert isinstance(categories, list)
    assert marshal(data, CategorySchema.category_list_doc)


def test_create_category(client):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/api/v1/category/' page is requested (POST)
    THEN check that the response is valid
    """
    res = client.post(
    	'/api/v1/category/',
    	json={"name": "medical"}
    )
    assert res.status_code == 200
    expected = {
        "category_id": 5,
        "category_name": "medical"
    }
    assert expected == json.loads(res.get_data(as_text=True))

def test_update_category(client):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/api/v1/category/' page is requested (POST)
    THEN check that the response is valid
    """
    res = client.put(
    	'/api/v1/category/5',
    	json={"name": "medical equipment"}
    )
    assert res.status_code == 200
    expected = {
        "category_id": 5,
        "category_name": "medical equipment"
    }
    assert expected == json.loads(res.get_data(as_text=True))