def is_valid_year(year: str) -> bool:
    if year.isdigit() and not year.startswith("0") and (int(year) >= 1900) and (int(year) <= 2100):
        return True
    else:
        return False


def is_valid_month(month: str) -> bool:
    if month.isdigit() and (int(month) >= 1) and (int(month) <= 12):
        return True
    else:
        return False


def format_month(month: str) -> str:
    if int(month) in {1, 2, 3, 4, 5, 6, 7, 8, 9}:
        formatted_month = "0" + month.lstrip("0")
    elif int(month) in {10, 11, 12}:
        formatted_month = month.lstrip("0")
    else:
        raise ValueError(f"Invalid month specified: {month}")
    return formatted_month


def days_in_month(month: str, year: str) -> str:
    if int(month) in {1, 3, 5, 7, 8, 10, 12}:
        days = "31"
    elif int(month) in {4, 6, 9, 11}:
        days = "30"
    elif int(month) == 2:
        if (int(year) % 400 == 0) and (int(year) % 100 == 0):
            days = "29"
        elif (int(year) % 4 == 0) and (int(year) % 100 != 0):
            days = "29"
        else:
            days = "28"
    else:
        raise ValueError(f"Invalid month specified: {month}")
    return days



def get_calendar_api_url_month(month: str, year: str) -> str:
    """Creates link to Svátkyapi.cz API for a specific month"""

    if not is_valid_year(year):
        raise ValueError(f"Invalid year specified: {year}")
    
    if not is_valid_month(month):
        raise ValueError(f"Invalid month specified: {month}")
    
    formatted_month = format_month(month)

    days = days_in_month(formatted_month, year)

    return f"https://svatkyapi.cz/api/day/{year}-{formatted_month}-01/interval/{days}"
