#display today's date
import datetime
print("Welcome to the Date Display Program!")
def date():
    today = datetime.date.today()
    return today.strftime("%d-%m-%Y")
print("Today's date is:", date())
def tomorrow():
    tomorrow = datetime.date.today() + datetime.timedelta(days=1)
    return tomorrow.strftime("%d-%m-%y")
print("Tomorrow's date is:", tomorrow())
def day_after_tomorrow():
    day_after_tomorrow = datetime.date.today() + datetime.timedelta(days=2)
    return day_after_tomorrow.strftime("%d-%m-%y")
print("The day after tomorrow's date is:", day_after_tomorrow())
