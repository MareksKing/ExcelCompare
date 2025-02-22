from models.ExcelFile import Excel
from models.Sheets import Sheet
from constants.emoji import EMOJIS
from comparator.SheetComparator import compare_sheet_name, compare_row_count, compare_column_count
from typing import Generator
import logging

log = logging.getLogger()


def get_sheet_count(excel1: Excel, excel2: Excel) -> [int, bool]:
    """
    Compares the provided excel files for the same amount of sheets in the files.
    This is due to the fact that we are comparing the sheet names we need to know if sheet count is the same for iteration.
    :param excel1: Excel
    :param excel2: Excel
    :returns: A tuple of the sheet amount in the excels and whether they were of the same amount or not.
        If the sheet amount was not the same we return the smaller sheet amount to later not need to compare the other excel file sheets after reaching the smaller number.
    :rtype: tuple[int,bool]
    """
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
    """
    Compares two lists of sheets and returns which was shorter together with a indicator which excel it belonged to.
    Also returns the compared against list of sheets which was longer.
    :param sheets1: list`[Sheet]`
    :param sheets2: list`[Sheet]`
    :returns: Two tuples, first being the shorter sheet list, second being longer sheet list.
    :rtype: tuple[list[Sheet],str]
    """

    if len(sheets1) < len(sheets2):
        return (sheets1, "Excel1"), (sheets2, "Excel2")

    if len(sheets1) > len(sheets2):
        return (sheets2, "Excel2"), (sheets1, "Excel1")


def compare_sheet_names_lists(excel1: Excel, excel2: Excel) -> list[str]:
    """
    Compare sheet names of the two provided excels and returns a list of strings,
    that shows if both excels had the same sheet in the same place or if they even had it at all.
    :param excel1: class:`Excel`
    :param excel2: class:`Excel`
    :returns: A list of strings containing the new sheet names for the resulting excel file
    :rtype: list[str]

    :Example:
    >>> excel1_sheet_names = ["A_sheet", "B_sheet", "C_sheet"]
    >>> excel2_sheet_names = ["B_sheet", "B_sheet"]
    >>> returns -> compared_sheet_names = ["'A_sheet' | 'B_sheet'", "B_sheet", "'C_sheet' | '❌'"]
    """
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
    """
    Compares two sheet column count and returns True if both sheets have the same amount of columns
    If that is not the case, then we return the different between the smaller column count and the bigger one.
    This difference will be used to determine the amount of columns we need to mark as different using the max columns function
    :param sheet1: class:`Sheet`
    :param sheet2: class:`Sheet`
    :returns: Either a bool if the column count was the same or an int that is the difference between the two sheets
    :rtype: `bool` or `int`
    """
    if compare_column_count(sheet1, sheet2):
        return True

    # If sheet column count differs then return amount of columns missing from the smallest one, and in the bigger excel mark the (max_column - missing_amount) in orange
    return abs(sheet1.columns - sheet2.columns)


def compare_sheet_rows(sheet1: Sheet, sheet2: Sheet) -> bool | int:
    """
    Compares two sheet row count and returns True if both sheets have the same amount of rows
    If that is not the case, then we return the different between the smaller row count and the bigger one.
    This difference will be used to determine the amount of rows we need to mark as different using the max rows function
    :param sheet1: class:`Sheet`
    :param sheet2: class:`Sheet`
    :returns: Either a bool if the row count was the same or an int that is the difference between the two sheets
    :rtype: `bool` or `int`
    """
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
            print(sheets1[i].sheet_name, "and", sheets2[i].sheet_name, "are of equal column size")
            result.append((i, sheets1[i].columns))
        else:
            print(sheets1[i].sheet_name, "and", sheets2[i].sheet_name,
                  "are not of equal column size")
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
            print(sheets1[i].sheet_name, "and", sheets2[i].sheet_name, "are of equal row size")
            result.append((i, sheets1[i].rows))
        else:
            print(sheets1[i].sheet_name, "and", sheets2[i].sheet_name, "are not of equal row size")
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


def compare_equal_lenght_list_items(items1: list, items2: list):
    result_val = []
    string = ""
    for items in zip(items1, items2):
        item1, item2 = items
        if item1 == item2:
            string = f"{str(item1)}"
        else:
            string = f"{EMOJIS.get('WARNING')} {str(item1)} | {str(item2)}"
        result_val.append(string)
    print("Result of equal lenght lists", result_val)
    return result_val


def determine_smaller_value_generator(values1: Generator, values2: Generator) -> (Generator, Generator):
    """
    Returns the smaller and bigger generator in order
    """
    if len(values1) > len(values2):
        return values2, values1
    else:
        return values1, values2


def compare_values(values1: Generator, values2: Generator):
    result_val = []
    val_list = []
    if len(values1) == len(values2):
        print("Value lenghts are the same")
        for items1, items2 in zip(values1, values2):
            if len(items1) == len(items2):
                result_val = compare_equal_lenght_list_items(items1, items2)
                val_list.append(result_val)
                result_val = []
    else:
        print("Value lenghts are not the same")
        smaller_gen, bigger_gen = determine_smaller_value_generator(values1, values2)
        for values in zip(smaller_gen, bigger_gen):
            list1, list2 = values
            # TODO: Fix this for uneven row/column count values
            for j, items in enumerate(list1):
                item1, item2 = items, list2[j]
                try:
                    if item1 == item2:
                        string = f"{str(item1)}"
                        result_val.append(string)
                    else:
                        string = f"{EMOJIS.get('WARNING')} {str(item1)} | {str(item2)}"
                        result_val.append(string)
                except IndexError:
                    string = f"{EMOJIS.get('WARNING')} {str(item1)} | ''"
                    result_val.append(string)
                val_list.append(result_val)
                result_val = []
               # for val in value:
               #     string = f"{EMOJIS.get('WARNING')} {str(val)} | ''"
               #     result_val.append(string)
               # val_list.append(result_val)
               # result_val = []
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


