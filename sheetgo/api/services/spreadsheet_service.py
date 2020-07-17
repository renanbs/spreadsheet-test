from openpyxl import load_workbook


class SpreadsheetException(Exception):
    pass


class SpreadsheetService:
    """
        The idea here is to create a service that could be used with injector.
        This has only one method and no constructor because it only extract the list of tabs of the Excel xlsx file.
    """
    @staticmethod
    def ordered_sheetnames(spreadsheet):
        try:
            wb = load_workbook(filename=spreadsheet)
        except Exception:
            raise SpreadsheetException('could not load workbook')

        return sorted(wb.sheetnames)
