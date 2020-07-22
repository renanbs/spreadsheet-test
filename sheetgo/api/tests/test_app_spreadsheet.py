import os
from http import HTTPStatus
from io import BytesIO
from unittest.mock import MagicMock

import pytest

from sheetgo.api.services.spreadsheet_service import SpreadsheetService, SpreadsheetServiceException
from sheetgo.api.utils import file_loader


@pytest.fixture
def empty_file():
    filename = os.path.join(os.path.dirname(__file__), 'resources', 'empty_file.xlsx')
    return file_loader(filename, True)


@pytest.fixture
def multiple_tabs_file():
    filename = os.path.join(os.path.dirname(__file__), 'resources', 'file.xlsx')
    return file_loader(filename, True)


def test_should_get_error_when_no_file_is_sent(api_client, headers):
    response = api_client.post('/excel/info', headers=headers)
    assert response.status_code == HTTPStatus.BAD_REQUEST
    assert response.json == {'error': 'a file is required'}


def test_should_not_load_empty_file(api_client, empty_file, headers):
    data = dict(file=(BytesIO(empty_file), 'empty_file.xlsx'),)

    response = api_client.post('/excel/info', data=data, headers=headers)
    assert response.status_code == HTTPStatus.BAD_REQUEST
    assert response.json == {'error': 'did you try to send a file?'}


def test_should_not_load_file_with_invalid_ext(api_client, invalid_file_ext, headers):
    data = dict(file=(BytesIO(invalid_file_ext), 'file.wrong_ext'),)

    response = api_client.post('/excel/info', data=data, headers=headers)
    assert response.status_code == HTTPStatus.BAD_REQUEST
    assert response.json == {'error': 'unsupported file format'}


def test_should_list_tabs(api_client, multiple_tabs_file, headers):
    data = dict(file=(BytesIO(multiple_tabs_file), 'file.xlsx'),)

    response = api_client.post('/excel/info', data=data, headers=headers)
    assert response.status_code == HTTPStatus.OK
    assert response.json == {'tabs': ['2009', '2010', 'A', 'B', 'Z']}


def test_should_not_load_workbook(injector, api_client, spreadsheet_service, multiple_tabs_file, headers):
    sp = injector.get(SpreadsheetService)
    sp.ordered_sheetnames = MagicMock(
        side_effect=SpreadsheetServiceException('some unknown exception happen'))

    data = dict(file=(BytesIO(multiple_tabs_file), 'file.xlsx'),)

    response = api_client.post('/excel/info', data=data, headers=headers)
    assert response.status_code == HTTPStatus.BAD_REQUEST
    assert response.json == {'error': 'some unknown exception happen'}


@pytest.mark.parametrize('headers, status, msg',
                         [(pytest.lazy_fixture('forbidden_headers'), HTTPStatus.FORBIDDEN, 'Forbidden'),
                          (pytest.lazy_fixture('invalid_headers'), HTTPStatus.UNAUTHORIZED,
                           'Signature verification failed')])
def test_should_validate_token(api_client, headers, status, msg):
    response = api_client.post('/excel/info', headers=headers)
    assert response.status_code == status
    assert response.json == {'error': msg}
