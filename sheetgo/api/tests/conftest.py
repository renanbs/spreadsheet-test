import os

import jwt
import pytest
from flask import Flask

from sheetgo.api.app import create_app
from sheetgo.api.utils import file_loader


@pytest.fixture
def app(injector) -> Flask:
    app = create_app(injector)
    app.config['TESTING'] = True
    app.config['SECRET_KEY'] = 'my secret key'

    return app


@pytest.fixture
def api_client(app):
    app.config['TESTING'] = True
    app.config['DEBUG'] = True
    return app.test_client()


@pytest.fixture
def invalid_file_ext():
    filename = os.path.join(os.path.dirname(__file__), 'resources', 'file.wrong_ext')
    return file_loader(filename, True)


@pytest.fixture
def token(app):
    return jwt.encode(payload={'email': 'rafael@sheetgo.com'}, key=app.config['SECRET_KEY']).decode('utf-8')


@pytest.fixture
def headers(token):
    return {'Authorization': f'Bearer {token}'}


@pytest.fixture
def forbidden_token(app):
    return jwt.encode(payload={'email': 'renan@sheetgo.com'}, key=app.config['SECRET_KEY']).decode('utf-8')


@pytest.fixture
def forbidden_headers(forbidden_token):
    return {'Authorization': f'Bearer {forbidden_token}'}


@pytest.fixture
def invalid_token():
    return jwt.encode(payload={'email': 'rafael@sheetgo.com'}, key='my invalid secret key').decode('utf-8')


@pytest.fixture
def invalid_headers(invalid_token):
    return {'Authorization': f'Bearer {invalid_token}'}
