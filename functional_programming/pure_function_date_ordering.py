def sensible_date(date):
    # order with slicing
    # new_date = date.split("-")
    # return new_date[-1:] + new_date[:-1]

    # order with numeric comparison
    month, day, year = date.split("-")
    return (int(year), int(month), int(day))


def sort_dates(dates):
    return sorted(dates, key=sensible_date)
