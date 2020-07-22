from http import HTTPStatus

from flask import Blueprint, jsonify, request

from injector import inject

from sheetgo.api.auth import requires_auth
from sheetgo.api.serializer import FileSerializer, FileSerializerException
from sheetgo.api.services.spreadsheet_service import SpreadsheetService, SpreadsheetServiceException
from sheetgo.dependencies import Application


class SpreadsheetEndpoint:

    @inject
    def __init__(self, app: Application, spreadsheet_service: SpreadsheetService):
        self.app = app
        self.spreadsheet_service = spreadsheet_service

    def register_endpoints(self):
        app_bp = Blueprint('SpreadsheetApp', __name__)

        @self.app.route('/excel/info', methods=['POST'])
        @requires_auth
        def extract_tabs():
            try:
                serializer = FileSerializer(request.files, ['xlsx'])
                serializer.is_valid()
                tabs = self.spreadsheet_service.ordered_sheetnames(request.files['file'])
            except (SpreadsheetServiceException, FileSerializerException) as ex:
                return jsonify({'error': str(ex)}), HTTPStatus.BAD_REQUEST

            return jsonify({'tabs': tabs}), HTTPStatus.OK

        return app_bp
