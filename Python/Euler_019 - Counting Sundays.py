# Project Euler Question 19 - Counting Sundays

import calendar  # the question is all about calendars
import time  # import for time calculation

start_time = time.time()  # start the clock

# Average solve time (M1 Mac) - 0.0009 sec


count = 0  # set initial counting value

for year in range(1901, 2001):  # loops from year 1901 to 2001
    for i in range(1, 13):  # loops through the months
        a = calendar.monthrange(year, i)
        if a[0] == 6:  # if the month starts with sunday
            count = count + 1


print("The number of sundays between 1901 to 2001 is:", count)
print("--- %s seconds ---" % (time.time() - start_time))

# End of code
