import openpyxl as opl
import os


class ExcelFinal:

    def __init__(self, sheet_names=[], rows=[], columns=[], values=[]):
        self.sheet_names = sheet_names
        self.rows = rows
        self.columns = columns
        self.values = values

    @property
    def get_file_path(self):
        FILE_NAME = "Compared_excel.xlsx"
        dir = os.getcwd()
        save_directory = os.path.join(dir, FILE_NAME)
        return save_directory

    def to_excel(self):
        wb = self.create_workbook()
        self.create_workbook_sheets(wb)

    def create_workbook(self):
        workbook = opl.Workbook()
        workbook.save(self.get_file_path)
        return workbook

    def create_workbook_sheets(self, workbook: opl.Workbook):
        sheets = self.sheet_names
        for i in range(0, len(sheets)):
            workbook.create_sheet(sheets[i], i)
        workbook.save(self.get_file_path)
