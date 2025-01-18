from models.ExcelFile import Excel
from models.Sheets import Sheet
from constants.emoji import EMOJIS
from comparator.SheetComparator import compare_sheet_name, compare_row_count, compare_column_count
from typing import Generator
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
                result.append(f"Excel1 {sheets1[i].sheet_name} | Excel2 {sheets2[i].sheet_name}")
            else:
                result.append(sheets1[i].sheet_name)
    else:
        # TODO! 🤮 clean up
        (smaller, smallerName), (bigger, biggerName) = get_smaller_sheet_amount(sheets1, sheets2)
        for i in range(0, len(smaller)):
            if not compare_sheet_name(sheets1[i], sheets2[i]):
                result.append(f"Excel1 {sheets1[i].sheet_name} | Excel2 {sheets2[i].sheet_name}")
            result.append(sheets1[i].sheet_name)
        for i in range(len(smaller), len(bigger)):
            if smallerName == "Excel1":
                result.append(f"Excel1 {EMOJIS.get('ERROR')} | Excel2 {sheets2[i].sheet_name}")
            if smallerName == "Excel2":
                result.append(f"Excel1 {sheets1[i].sheet_name} | Excel2 {EMOJIS.get('ERROR')}")

    return result


def compare_sheet_columns(sheet1: Sheet, sheet2: Sheet) -> bool | int:
    if compare_column_count(sheet1, sheet2):
        return True

    # If sheet column count differs then return amount of columns missing from the smallest one, and in the bigger excel mark the (max_column - missing_amount) in orange
    return abs(sheet1.columns - sheet2.columns)


def compare_sheet_rows(sheet1: Sheet, sheet2: Sheet) -> bool | int:
    if compare_row_count(sheet1, sheet2):
        return True

    # If sheet column count differs then return amount of columns missing from the smallest one, and in the bigger excel mark the (max_column - missing_amount) in orange
    return abs(sheet1.rows - sheet2.rows)


def compare_sheet_columns_dim(excel1: Excel, excel2: Excel):
    sheetCount, same_amount = get_sheet_count(excel1, excel2)
    sheets1 = excel1.sheets
    sheets2 = excel2.sheets
    result = []
    for i in range(0, sheetCount):
        sheet_compare = compare_sheet_columns(sheets1[i], sheets2[i])
        if isinstance(sheet_compare, bool):
            continue
        result.append((i, sheet_compare))
    if not same_amount:
        max_sheet_count = max(len(sheets1), len(sheets2))
        for i in range(sheetCount, max_sheet_count):
            result.append((i, 0))
    return result


def compare_sheet_rows_dim(excel1: Excel, excel2: Excel):
    sheetCount, same_amount = get_sheet_count(excel1, excel2)
    sheets1 = excel1.sheets
    sheets2 = excel2.sheets
    result = []
    for i in range(0, sheetCount):
        sheet_compare = compare_sheet_rows(sheets1[i], sheets2[i])
        if isinstance(sheet_compare, bool):
            continue
        result.append((i, sheet_compare))
    if not same_amount:
        max_sheet_count = max(len(sheets1), len(sheets2))
        for i in range(sheetCount, max_sheet_count):
            result.append((i, 0))
    return result


def get_sheet_values(sheet1: Sheet, sheet2: Sheet):
    sheet1Values = sheet1.values
    sheet2Values = sheet2.values
    return sheet1Values, sheet2Values


def compare_values(values1: Generator, values2: Generator):
    string = ""
    result_val = []
    val_list = []
    for values in zip(values1, values2):
        list1, list2 = values
        for items in zip(list1, list2):
            item1, item2 = items
            if item1 == item2:
                string = f"{str(item1)}"
            else:
                string = f"{EMOJIS.get('WARNING')} {str(item1)} | {str(item2)}"
            result_val.append(string)
        val_list.append(result_val)
    return val_list


def compare_sheet_values(excel1: Excel, excel2: Excel):
    sheetCount, same_amount = get_sheet_count(excel1, excel2)
    sheets1 = excel1.sheets
    sheets2 = excel2.sheets
    result = []
    for i in range(0, sheetCount):
        values1, values2 = get_sheet_values(sheets1[i], sheets2[i])
        result.append(compare_values(values1, values2))
    return result


