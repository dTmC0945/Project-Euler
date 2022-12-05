import calendar  # the question is all about calendars


count = 0

for year in range(1901, 2001):
    for i in range(1, 13):
        a = calendar.monthrange(year, i)
        if a[0] == 6:
            count = count + 1


print(count)
