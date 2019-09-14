import datetime
import calendar

def findDay(date):
    day = datetime.datetime.strptime(date, '%m %d %Y').weekday()
    return (calendar.day_name[day])

date = input()
print(findDay(date).upper())
