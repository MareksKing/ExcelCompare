from models.Sheets import Sheet


def compare_all_sheet_properties(sheet1: Sheet, sheet2: Sheet) -> bool:
    """
    Returns True if both provided sheets are the same comparing attributes
    :param sheet1: Sheet
    :param sheet2: Sheet
    :return: bool
    """
    return sheet1 == sheet2


def compare_sheet_name(sheet1: Sheet, sheet2: Sheet) -> bool:
    """
    Returns True if both provided sheet names are the same
    :param sheet1: Sheet
    :param sheet2: Sheet
    :return: bool
    """
    return sheet1.sheet_name == sheet2.sheet_name


def compare_row_count(sheet1: Sheet, sheet2: Sheet) -> bool:
    """
    Returns True if both provided sheet row counts are the same
    :param sheet1: Sheet
    :param sheet2: Sheet
    :return: bool
    """
    return sheet1.rows == sheet2.rows


def compare_column_count(sheet1: Sheet, sheet2: Sheet) -> bool:
    """
    Returns True if both provided sheet column counts are the same
    :param sheet1: Sheet
    :param sheet2: Sheet
    :return: bool
    """
    return sheet1.columns == sheet2.columns


def compare_values(sheet1: Sheet, sheet2: Sheet) -> bool:
    """
    Returns True if both provided sheet values are the same
    :param sheet1: Sheet
    :param sheet2: Sheet
    :return: bool
    """
    return sheet1.values == sheet2.values

