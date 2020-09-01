from datetime import date, timedelta


class Weekday:
    MONDAY = 0
    TUESDAY = 1
    WEDNESDAY = 2
    THURSDAY = 3
    FRIDAY = 4
    SATURDAY = 5
    SUNDAY = 6


def meetup_date(year: int, month: int, nth: int=4, weekday: int=Weekday.THURSDAY):
    """Returns date representing nth weekday of the given year and month"""

    if month not in range(1, 13):
        raise ValueError("month not in range 1-12")

    if nth == 0:
        raise ValueError("nth cannot be 0")

    if weekday not in range(7):
        raise ValueError("weekday not in range 0-6")

    # calculate nth weekday day
    if nth > 0:
        # based on first day of the month
        month_first_weekday = date(year, month, 1).weekday()
        first_weekday_day = 1 + (weekday - month_first_weekday + 7) % 7
        nth_weekday_day = first_weekday_day + (nth - 1) * 7
    else:
        # based on last day of the month
        if month == 12:
            month_last_date = date(year + 1, 1, 1) - timedelta(days=1)
        else:
            month_last_date = date(year, month + 1, 1) - timedelta(days=1)
        
        last_weekday_day = month_last_date.day - (month_last_date.weekday() - weekday + 7) % 7
        nth_weekday_day = last_weekday_day - abs(nth + 1) * 7
    
    return date(year, month, nth_weekday_day)
