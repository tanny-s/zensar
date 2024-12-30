import calendar as cal
def month_cal(year, month):
    if month < 1 or month > 12:
        print("Invalid month. Please enter a month between 1 and 12.")
        return
    first_day, num_days = cal.monthrange(year, month)
    # Print the header with the month and year
    print(f"\nCalendar for {cal.month_name[month]} {year}")
    
    # Print leading spaces for the first week to align the dates correctly
    print("   " * first_day, end="")
    
    # Print each day of the month
    for day in range(1, num_days + 1):
        # Print the day with two digits, followed by a space
        print(f"{day:2} ", end="")
        
        # If it's the end of the week (Sunday), start a new line
        if (first_day + day) % 7 == 0:
            print()

    print()