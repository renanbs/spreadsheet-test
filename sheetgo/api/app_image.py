from http import HTTPStatus

from flask import Blueprint, request, Response, jsonify

from injector import inject

from sheetgo.api.serializer import FileSerializer, FileSerializerException
from sheetgo.api.services.image_service import ImageService, ImageServiceException
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
            try:
                serializer = FileSerializer(request.files, ['jpeg', 'jpg', 'png'], request.form)
                serializer.is_valid()

                converted_image = self.image_service.convert_image(request.files['file'], request.form['format'])
            except (ImageServiceException, FileSerializerException) as ex:
                return jsonify({'error': str(ex)}), HTTPStatus.BAD_REQUEST

            filename = f'{request.files["file"]}.{request.form["format"]}'
            headers = {'Content-Disposition': f'attachment; filename="{filename}"'}
            return Response(converted_image, mimetype="image/png", direct_passthrough=True, headers=headers)

        return app_bp
