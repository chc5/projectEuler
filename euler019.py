import time
# Sunday = 0 Monday = 1 ... Saturday = 6
# Given that Jan 1 is a Monday on 1900
def get_num_days_of_year(year):
    if year % 4 == 0 and (not year % 100 == 0 or year % 400 == 0):
        return 366
    else:
        return 365
def is_leap_year(year):
    if year % 4 == 0 and (not year % 100 == 0 or year % 400 == 0):
        return True
    else:
        return False
def count_sundays_on_first_day(start_year,end_year):
    num_of_sundays = 0
    first_day_of_month = 1
    for year in range(1900,start_year):
        days_in_year = get_num_days_of_year(year)
        first_day_of_month = (first_day_of_month + days_in_year) % 7
    for year in range(start_year,end_year+1):
        day = 0
        for month in range(1,13):
            if month == 2:
                if is_leap_year(year):
                    first_day_of_month = (first_day_of_month + 29) % 7
                else:
                    first_day_of_month = (first_day_of_month + 28) % 7
            elif month == 9 or month == 4 or month == 11 or month == 6:
                first_day_of_month = (first_day_of_month + 30) % 7
            else:
                first_day_of_month = (first_day_of_month + 31) % 7
            if first_day_of_month == 0:
                num_of_sundays += 1
    return num_of_sundays
if __name__ == '__main__':
    start_time = time.time()
    print(count_sundays_on_first_day(1901,2000))
    end_time = time.time()
    print("Time Taken:",(end_time-start_time)*10**6,"microseconds")
