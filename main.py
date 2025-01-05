import pandas as pd
import openpyxl
from pprint import pp
import logging

from models.ExcelFile import Excel
from comparator.SheetComparator import compare_all_sheet_properties, compare_sheet_name
from constants.emoji import EMOJIS

log = logging.getLogger(__name__)


def main():
    log.info("Reading the excel files")
    file1 = "excel1.xlsx"
    file2 = "excel2.xlsx"
    excel: Excel = Excel(file_path=file1)
    excel2: Excel = Excel(file_path=file2)

    log.info("Getting the sheet count")

    for i in range(0, sheetCount):
        sheet1 = excel.sheets[i]
        sheet2 = excel2.sheets[i]
        log.info("Comparing the sheet values")

        if compare_all_sheet_properties(sheet1, sheet2):
            log.info("All sheet properties are the same")
            log.info(f"{sheet1.sheet_name} - {EMOJIS.get('CHECKMARK')}")
            log.info(f"{sheet2.sheet_name} - {EMOJIS.get('CHECKMARK')}")
            continue

        log.info("Some properties are not the same")

        if not compare_sheet_name(sheet1, sheet2):
            log.info("Sheet names are not the same")
            log.info(f"{sheet1.sheet_name} - {EMOJIS.get('ERROR')}")
            log.info(f"{sheet2.sheet_name} - {EMOJIS.get('ERROR')}")
            continue
        log.info("Sheet names are the same but some other property differs")

        log.info(f"{sheet1.sheet_name} - {EMOJIS.get('WARNING')}")
        log.info(f"{sheet2.sheet_name} - {EMOJIS.get('WARNING')}")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    main()
