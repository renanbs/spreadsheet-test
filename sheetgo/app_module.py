from injector import Module, singleton, provider

from sheetgo.api.app_image import ImageEndpoint
from sheetgo.api.app_spreadsheet import SpreadsheetEndpoint
from sheetgo.api.services.SpreadsheetService import SpreadsheetService
from sheetgo.default import Config
from sheetgo.dependencies import ApplicationRegister, ApplicationConfig


class AppModule(Module):
    @singleton
    @provider
    def register(self) -> ApplicationRegister:
        return [SpreadsheetEndpoint, ImageEndpoint]

    @provider
    def configuration(self) -> ApplicationConfig:
        return Config

    @provider
    def spreadsheet_service(self) -> SpreadsheetService:
        return SpreadsheetService()
