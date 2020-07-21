import pytest

from injector import Injector, InstanceProvider

from sheetgo.api.services.image_service import ImageService
from sheetgo.api.services.spreadsheet_service import SpreadsheetService
from sheetgo.main_module import MODULES


@pytest.fixture
def injector(spreadsheet_service):
    injector = Injector(MODULES)
    injector.binder.bind(SpreadsheetService, to=InstanceProvider(spreadsheet_service))
    injector.binder.bind(ImageService, to=InstanceProvider(image_service))
    yield injector


@pytest.fixture
def spreadsheet_service():
    return SpreadsheetService()


@pytest.fixture
def image_service():
    return ImageService()
