from http import HTTPStatus


from flask import Blueprint, jsonify

from injector import inject

from sheetgo.dependencies import Application


class SpreadsheetEndpoint:

    @inject
    def __init__(self, app: Application):
        self.app = app

    def register_endpoints(self):
        app_bp = Blueprint('SpreadsheetApp', __name__, static_url_path='/apidocs')

        @self.app.route("/myping", methods=['GET'])
        def myping():
            return jsonify({'ok': 'ok'}), HTTPStatus.OK

        @self.app.route('/excel/info', methods=['POST'])
        def extract_tabs():
            return jsonify({'ok': 'ok'}), HTTPStatus.OK

        return app_bp
