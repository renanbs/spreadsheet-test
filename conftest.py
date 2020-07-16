import pytest
from injector import Injector

from sheetgo.main_module import MODULES


@pytest.fixture
def injector():
    injector = Injector(MODULES)

    yield injector
