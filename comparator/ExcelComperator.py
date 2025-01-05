from models.ExcelFile import Excel


def get_sheet_amount(Excel1: Excel, Excel2: Excel) -> int:


def compare_all_sheet_names(Excel1: Excel, Excel2: Excel) -> bool:
    sheets1 = Excel1.sheets.sort(key=str.lower())
    sheets2 = Excel2.sheets.sort(key=str.lower())
