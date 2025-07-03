import requests
import sys
import calendar_api


#date = sys.argv[1]
date = "2025-06-01"
month = date[5:7].lstrip("0")
api_url = calendar_api.get_calendar_api_url_month("06", "2025")
#print(api_url)


response = requests.get(api_url)
response.raise_for_status()

days = [day for day in response.json() if day["monthNumber"] == month]

for day in days:
    if day["isHoliday"]:
        work = "státní svátek"
    elif day["dayInWeek"] == "sobota" or day["dayInWeek"] == "neděle":
        work = "víkend"
    else:
        work = "8:30-12:00;  12:30-17:00  (8 hod)"
    print(f"{day['date']}    {work}")


# TODO unit tests, Day class, abstraction - get_api_url(), error handling, input validation, annual leave, defaults
