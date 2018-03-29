import time
# Sunday = 0 Monday = 1 ... Saturday = 6
# Given that Jan 1 is a Monday on 1900
def getNumDaysOfYear(year):
    if year % 4 == 0 and (not year % 100 == 0 or year % 400 == 0):
        return 366
    else:
        return 365
def isLeapYear(year):
    if year % 4 == 0 and (not year % 100 == 0 or year % 400 == 0):
        return True
    else:
        return False
def countingSundaysOnJan(start_year,end_year):
    numOfSundays = 0
    firstDayOfMonth = 1
    for year in range(1900,start_year):
        daysInYear = getNumDaysOfYear(year)
        firstDayOfMonth = (firstDayOfMonth + daysInYear) % 7
    for year in range(start_year,end_year+1):
        day = 0
        for month in range(1,13):
            if month == 2:
                if isLeapYear(year):
                    firstDayOfMonth = (firstDayOfMonth + 29) % 7
                else:
                    firstDayOfMonth = (firstDayOfMonth + 28) % 7
            elif month == 9 or month == 4 or month == 11 or month == 6:
                firstDayOfMonth = (firstDayOfMonth + 30) % 7
            else:
                firstDayOfMonth = (firstDayOfMonth + 31) % 7
            if firstDayOfMonth == 0:
                numOfSundays += 1
    return numOfSundays
if __name__ == '__main__':
    start_time = time.time()
    print(countingSundaysOnJan(1901,2000))
    end_time = time.time()
    print("Time Taken:",end_time-start_time)
