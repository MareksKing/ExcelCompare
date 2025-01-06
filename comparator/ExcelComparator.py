from models.ExcelFile import Excel
from models.Sheets import Sheet
from constants.emoji import EMOJIS
from comparator.SheetComparator import compare_sheet_name, compare_row_count, compare_column_count
import logging

log = logging.getLogger()


def get_sheet_count(excel1: Excel, excel2: Excel) -> [int, bool]:
    sheetCount = 0
    same_amount = False
    if len(excel1.sheets) == len(excel2.sheets):
        log.debug("Sheet count is the same")
        sheetCount = len(excel1.sheets)
        same_amount = True
    else:
        log.debug("Sheet count is not the same, getting the lowest amount")
        sheetCount = min(len(excel1.sheets), len(excel2.sheets))
        same_amount = False
    return sheetCount, same_amount


def get_smaller_sheet_amount(sheets1: list[Sheet], sheets2: list[Sheet]) -> (list[Sheet], str):

    if len(sheets1) < len(sheets2):
        return (sheets1, "Excel1"), (sheets2, "Excel2")

    if len(sheets1) > len(sheets2):
        return (sheets2, "Excel2"), (sheets1, "Excel1")


def compare_sheet_names_lists(excel1: Excel, excel2: Excel) -> list[str]:
    sheetCount, same_amount = get_sheet_count(excel1, excel2)
    sheets1 = excel1.sheets
    sheets2 = excel2.sheets
    result = []
    if same_amount:
        for i in range(0, sheetCount):
            if not compare_sheet_name(sheets1[i], sheets2[i]):
                result.append(f"Excel1: {sheets1[i].sheet_name} | Excel2: {sheets2.sheet_name}")
            result.append(sheets1[i].sheet_name)
    else:
        # TODO! 🤮 clean up
        (smaller, smallerName), (bigger, biggerName) = get_smaller_sheet_amount(sheets1, sheets2)
        for i in range(0, len(smaller)):
            if not compare_sheet_name(sheets1[i], sheets2[i]):
                result.append(f"Excel1: {sheets1[i].sheet_name} | Excel2: {sheets2.sheet_name}")
            result.append(sheets1[i].sheet_name)
        for i in range(len(smaller), len(bigger)):
            if smallerName == "Excel1":
                result.append(f"Excel1: {EMOJIS.get('ERROR')} | Excel2: {sheets2[i].sheet_name}")
            if smallerName == "Excel2":
                result.append(f"Excel1: {sheets1[i].sheet_name} | Excel2: {EMOJIS.get('ERROR')}")

    return result


def compare_sheet_dimensions(excel1: Excel, excel2: Excel):
    # TODO! COMPARE SHEET DIMENSIONS ROWS AND COLUMNS FUTURE MAREK
    sheetCount, same_amount = get_sheet_count(excel1, excel2)
    sheets1 = excel1.sheets
    sheets2 = excel2.sheets
    result = []
    if same_amount:
        for i in range(0, sheetCount):
            if compare_column_count(sheets1[i], sheets2[i]):
                continue
