import pandas as pd
import openpyxl
from pprint import pp

from models.ExcelFile import Excel


def main():
    file1 = "excel1.xlsx"
    file2 = "excel1.xlsx"
    excel: Excel = Excel(file_path=file1)
    excel2: Excel = Excel(file_path=file2)

    print(excel.sheets)


if __name__ == "__main__":
    main()
