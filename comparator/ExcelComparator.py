from models.ExcelFile import Excel
from constants.emoji import EMOJIS
from comparator.SheetComparator import compare_sheet_name
import logging

log = logging.getLogger()


def get_sheet_count(excel1: Excel, excel2: Excel) -> int:
    sheetCount = 0
    if len(excel1.sheets) == len(excel2.sheets):
        log.debug("Sheet count is the same")
        sheetCount = len(excel1.sheets)
    else:
        log.debug("Sheet count is not the same, getting the lowest amount")
        sheetCount = min(len(excel1.sheets), len(excel2.sheets))
    return sheetCount


def compare_sheet_names_lists(excel1: Excel, excel2: Excel, sheetCount: int) -> bool:
    sheets1 = excel1.sheets.sort(key=str.lower())
    sheets2 = excel2.sheets.sort(key=str.lower())
    # TODO: Think of a better way

    for i in range(0, sheetCount):
        if not compare_sheet_name(sheets1[i], sheets2[i]):
            return False
    return True
