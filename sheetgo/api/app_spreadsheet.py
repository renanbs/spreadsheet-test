from http import HTTPStatus

from flask import Blueprint, jsonify, request

from injector import inject

from sheetgo.api.services.SpreadsheetService import SpreadsheetService, SpreadssheetException
from sheetgo.dependencies import Application


class SpreadsheetEndpoint:

    @inject
    def __init__(self, app: Application, spreadsheet_service: SpreadsheetService):
        self.app = app
        self.spreadsheet_service = spreadsheet_service

    def register_endpoints(self):
        app_bp = Blueprint('SpreadsheetApp', __name__)

        @self.app.route('/excel/info', methods=['POST'])
        def extract_tabs():
            if 'file' not in request.files:
                return {'error': 'invalid file'}, HTTPStatus.BAD_REQUEST

            the_file = request.files['file']
            if the_file.filename == '' or the_file.content_length == 0:
                return {'error': 'did you try to send a file?'}, HTTPStatus.BAD_REQUEST

            try:
                tabs = self.spreadsheet_service.ordered_sheetnames(the_file)
            except SpreadssheetException as ex:
                return jsonify({'error': str(ex)}), HTTPStatus.BAD_REQUEST

            return jsonify({'tabs': tabs}), HTTPStatus.OK

        return app_bp
