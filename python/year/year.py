from calendar import calendar as cal
def year():
    year=int(input("enter the year"))
    print(f"\nEnter Calendar for year {year}:")
    print(cal.calendar(year))
    return 0