import os
from http import HTTPStatus
from io import BytesIO
from unittest.mock import MagicMock

import pytest

from sheetgo.api.services.image_service import ImageService, ImageServiceException
from sheetgo.api.utils import file_loader


@pytest.fixture
def empty_file():
    filename = os.path.join(os.path.dirname(__file__), 'resources', 'empty_file.png')
    return file_loader(filename, True)


@pytest.fixture
def simple_jpg():
    filename = os.path.join(os.path.dirname(__file__), 'resources', 'tux.jpg')
    return file_loader(filename, True)


def test_should_get_error_if_no_file_is_sent(api_client, headers):
    response = api_client.post('/image/convert', headers=headers)
    assert response.status_code == HTTPStatus.BAD_REQUEST
    assert response.json == {'error': 'a file is required'}


def test_should_not_load_empty_file(api_client, empty_file, headers):
    data = dict(file=(BytesIO(empty_file), 'empty_file.png'),)

    response = api_client.post('/image/convert', data=data, headers=headers)
    assert response.status_code == HTTPStatus.BAD_REQUEST
    assert response.json == {'error': 'did you try to send a file?'}


def test_should_not_load_file_with_invalid_ext(api_client, invalid_file_ext, headers):
    data = dict(file=(BytesIO(invalid_file_ext), 'file.wrong_ext'),)

    response = api_client.post('/image/convert', data=data, headers=headers)
    assert response.status_code == HTTPStatus.BAD_REQUEST
    assert response.json == {'error': 'unsupported file format'}


def test_should_not_load_file_with_invalid_request_format(api_client, invalid_file_ext, headers):
    data = dict(file=(BytesIO(invalid_file_ext), 'file.wrong_ext'),)

    response = api_client.post('/image/convert', data=data, headers=headers)
    assert response.status_code == HTTPStatus.BAD_REQUEST
    assert response.json == {'error': 'unsupported file format'}


def test_should_convert_image(api_client, simple_jpg, headers):
    data = dict(file=(BytesIO(simple_jpg), 'tux.jpg'), format='png')

    response = api_client.post('/image/convert', data=data, headers=headers)
    assert response.status_code == HTTPStatus.OK
    assert response.content_type == 'image/png'


def test_should_not_convert_image_without_format(api_client, simple_jpg, headers):
    data = dict(file=(BytesIO(simple_jpg), 'tux.jpg'))

    response = api_client.post('/image/convert', data=data, headers=headers)
    assert response.status_code == HTTPStatus.BAD_REQUEST
    assert response.json == {'error': 'a format is required'}


def test_should_not_convert_image(injector, api_client, image_service, simple_jpg, headers):
    sp = injector.get(ImageService)
    sp.convert_image = MagicMock(
        side_effect=ImageServiceException('some unknown exception happen'))

    data = dict(file=(BytesIO(simple_jpg), 'tux.jpg'), format='png')

    response = api_client.post('/image/convert', data=data, headers=headers)
    assert response.status_code == HTTPStatus.BAD_REQUEST
    assert response.json == {'error': 'some unknown exception happen'}


@pytest.mark.parametrize('headers, status, msg',
                         [(pytest.lazy_fixture('forbidden_headers'), HTTPStatus.FORBIDDEN, 'Forbidden'),
                          (pytest.lazy_fixture('invalid_headers'), HTTPStatus.UNAUTHORIZED,
                           'Signature verification failed')])
def test_should_validate_token(api_client, headers, status, msg):
    response = api_client.post('/image/convert', headers=headers)
    assert response.status_code == status
    assert response.json == {'error': msg}
