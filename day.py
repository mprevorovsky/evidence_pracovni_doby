from dataclasses import dataclass

@dataclass
class Day:
    date: str
    day_number: int
    day_in_week: str
    month_number: int
    month: dict["nominative": str, "genitive": str]
    year: int
    name: str
    is_holiday: bool
    holiday_name: str

