from http import HTTPStatus

from flask import Blueprint, request, Response

from injector import inject

from sheetgo.api.services.image_service import ImageService
from sheetgo.api.utils import validate_zero_file_size, split_filename
from sheetgo.dependencies import Application


class ImageEndpoint:

    @inject
    def __init__(self, app: Application, image_service: ImageService):
        self.app = app
        self.image_service = image_service

    def register_endpoints(self):
        app_bp = Blueprint('ImageApp', __name__)

        @self.app.route('/image/convert', methods=['POST'])
        def convert_image():
            if 'file' not in request.files:
                return {'error': 'invalid file'}, HTTPStatus.BAD_REQUEST

            the_file = request.files['file']
            if the_file.filename == '' or not validate_zero_file_size(the_file):
                return {'error': 'did you try to send a file?'}, HTTPStatus.BAD_REQUEST

            filename, file_ext = split_filename(the_file.filename)
            if file_ext not in ['.jpeg', '.jpg', '.png']:
                return {'error': 'unsupported file format'}, HTTPStatus.BAD_REQUEST

            file_format = request.form['format']
            if file_format not in ['.jpeg', '.jpg', '.png']:
                return {'error': 'unsupported conversion format'}, HTTPStatus.BAD_REQUEST

            converted_image = self.image_service.convert_image(the_file, file_format)

            headers = {'Content-Disposition': f'attachment; filename="{filename}.{file_format}"'}
            return Response(converted_image, mimetype="image/png", direct_passthrough=True, headers=headers)

        return app_bp
