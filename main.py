import logging

from models.ExcelFile import Excel
from models.CreatedExcel import ExcelFinal
from comparator.SheetComparator import compare_all_sheet_properties, compare_sheet_name
from comparator.ExcelComparator import compare_sheet_names_lists, compare_sheet_columns_dim, compare_sheet_rows_dim, compare_sheet_values


log = logging.getLogger(__name__)


def main():
    log.info("Reading the excel files")
    file1 = "excel1.xlsx"
    file2 = "excel2.xlsx"
    excel: Excel = Excel(file_path=file1)
    excel2: Excel = Excel(file_path=file2)

    log.info("Getting the sheet count")

    result_sheet_names = compare_sheet_names_lists(excel, excel2)
    result_sheet_columns = compare_sheet_columns_dim(excel, excel2)
    result_sheet_rows = compare_sheet_rows_dim(excel, excel2)
    result_sheet_values = compare_sheet_values(excel, excel2)

    print(result_sheet_names)
    print(result_sheet_columns)
    print(result_sheet_rows)
    print(result_sheet_values)

    final_excel = ExcelFinal(result_sheet_names, result_sheet_rows,
                             result_sheet_columns, result_sheet_values)
    final_excel.to_excel()


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    main()
