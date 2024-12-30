import pandas as pd
import openpyxl
from pprint import pp
from models.ExcelFile import Excel

def main():
    file1 = "excel1.xlsx"
    excel: Excel = Excel(file_path=file1)
    # pp(excel.describe())
    for i in excel.sheets[0].values:
        print(i)

if __name__ == "__main__":
    main()
