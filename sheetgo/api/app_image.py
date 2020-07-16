from http import HTTPStatus


from flask import Blueprint, jsonify

from injector import inject

from sheetgo.dependencies import Application


class ImageEndpoint:

    @inject
    def __init__(self, app: Application):
        self.app = app

    def register_endpoints(self):
        app_bp = Blueprint('ImageApp', __name__)

        @self.app.route('/image/convert', methods=['POST'])
        def convert_image():
            return jsonify({'ok': 'ok'}), HTTPStatus.OK

        return app_bp
