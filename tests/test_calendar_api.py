import calendar_api


def test_is_valid_year():
    assert calendar_api.is_valid_year("2025") == True
    assert calendar_api.is_valid_year("2101") == False
    assert calendar_api.is_valid_year("1899") == False
    assert calendar_api.is_valid_year("02025") == False
    assert calendar_api.is_valid_year("test") == False


# def test_get_calendar_api_url():
#     date = "2025-05-01"
#     assert calendar_api.get_calendar_api_url_month(date) == "https://svatkyapi.cz/api/day/2025-05-01/interval/31"