import pandas as pd
import openpyxl
from pprint import pp
import logging

from models.ExcelFile import Excel
from comparator.SheetComparator import compare_all_sheet_properties, compare_sheet_name
from comparator.ExcelComparator import compare_sheet_names_lists
from constants.emoji import EMOJIS

log = logging.getLogger(__name__)


def main():
    log.info("Reading the excel files")
    file1 = "excel1.xlsx"
    file2 = "excel2.xlsx"
    excel: Excel = Excel(file_path=file1)
    excel2: Excel = Excel(file_path=file2)

    log.info("Getting the sheet count")

    compared_sheets = compare_sheet_names_lists(excel, excel2)
    print(compared_sheets)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    main()
