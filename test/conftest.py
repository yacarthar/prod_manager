"""default fixtures for unit testing
scope: package
"""
import os
import pytest
import psycopg2

from app import create_app


@pytest.fixture(scope="package")
def truncate_db(request):
    with psycopg2.connect(os.environ.get("PSYCOPG2_TEST")) as conn:
        with conn.cursor() as cur:
            with open("test\\db_clear.sql") as f:
                command = f.read()
                cur.execute(command)
                conn.commit()

    yield True


@pytest.fixture(scope="package", autouse=True)
def client(truncate_db):
    app = create_app()
    with app.app_context():
        with app.test_client() as testing_client:
            yield testing_client
