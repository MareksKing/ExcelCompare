from openpyxl import worksheet


def compare_sheet_properties(sheet1: worksheet, sheet2: worksheet) -> bool:
    return sheet1 == sheet2
