from models.Sheets import Sheet
from comparator.SheetComparator import compare_all_sheet_properties


class TestComparison:

    def test_same_sheet(self):
        sheet1: Sheet = Sheet(sheet_name="Sheet1", rows=1, columns=6, values=["A", "B", "C"])
        sheet2: Sheet = Sheet(sheet_name="Sheet1", rows=1, columns=6, values=["A", "B", "C"])

        assert compare_all_sheet_properties(sheet1, sheet2) is True

    def test_different_values(self):
        sheet1: Sheet = Sheet(sheet_name="Sheet1", rows=1, columns=6, values=["A", "B", "C"])
        sheet2: Sheet = Sheet(sheet_name="Sheet1", rows=1, columns=6, values=["m", "k", "D"])

        assert compare_all_sheet_properties(sheet1, sheet2) is False

    def test_different_sheet_params_rows(self):
        sheet1: Sheet = Sheet(sheet_name="Sheet1", rows=1, columns=6, values=["A", "B", "C"])
        sheet2: Sheet = Sheet(sheet_name="Sheet1", rows=2, columns=6, values=["A", "B", "C"])

        assert compare_all_sheet_properties(sheet1, sheet2) is False

    def test_different_sheet_params_cols(self):
        sheet1: Sheet = Sheet(sheet_name="Sheet1", rows=1, columns=6, values=["A", "B", "C"])
        sheet2: Sheet = Sheet(sheet_name="Sheet1", rows=1, columns=8, values=["A", "B", "C"])

        assert compare_all_sheet_properties(sheet1, sheet2) is False

    def test_different_sheet_params_name(self):
        sheet1: Sheet = Sheet(sheet_name="Sheet1", rows=1, columns=6, values=["A", "B", "C"])
        sheet2: Sheet = Sheet(sheet_name="Sheet2", rows=1, columns=6, values=["A", "B", "C"])

        assert compare_all_sheet_properties(sheet1, sheet2) is False

