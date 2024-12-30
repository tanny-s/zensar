import calendar as cal

def month():
    year = int(input("Enter year: "))
    month = int(input("Enter month (1-12): "))

    print(f"\nCalendar for {cal.month_name[month]} {year}:")
    print(cal.month(year, month))
    return 0