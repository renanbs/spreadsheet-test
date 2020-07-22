import os

import pytest
from flask import Flask

from sheetgo.api.app import create_app
from sheetgo.api.utils import file_loader


@pytest.fixture
def app(injector) -> Flask:
    app = create_app(injector)
    app.config['TESTING'] = True

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
