"""module from the official flask documentation"""

import pytest
from flaskr import create_app

@pytest.fixture()
def app():
    """fixture for our app"""
    app = create_app() #pylint disable = W0621
    app.config.update({
        "TESTING": True,
    })

    # other setup can go here

    yield app

    # clean up / reset resources here

@pytest.fixture()
def client(app):#pylint disable = W0621
    """fixture for our client that will make the tests"""
    return app.test_client()

@pytest.fixture()
def runner(app):#pylint disable = W0621
    """fixture for the runner"""
    return app.test_cli_runner()