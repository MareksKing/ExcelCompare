from dataclasses import dataclass
from openpyxl import worksheet
from typing import Generator

@dataclass
class Sheet:

    sheet_name: str
    rows: int
    columns: int
    values: Generator


