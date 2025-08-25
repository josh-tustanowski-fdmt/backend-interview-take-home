from typing import Tuple
import datetime as dt

def get_tax_year_dates(tax_year: int) -> Tuple[dt.date, dt.date]:
    sd = dt.date(tax_year, 4, 6)
    ed = dt.date(tax_year + 1, 4, 5)
    return sd, ed

def get_tax_year_from_date(date: dt.date) -> int:
    year = date.year
    if date.month <= 4 and date.day <= 5:
        return year - 1
    return year
