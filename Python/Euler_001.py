# Project Euler Question 1 - Multiples of 3 or 5

import time  # import for time calculation

start_time = time.time()  # start the clock

# Average solve time (M1 Mac) - 0.0001 sec

total = 0  # Declare a variable to keep tally on the sum

# Check if a number is divisible by either 3 or 5.
for index in range(1, 1000):
    if index % 3 == 0 or index % 5 == 0:
        total = index + total

print("The sum of all the multiples of 3 or 5 below 1000 is:", total)

print("--- %s seconds ---" % (time.time() - start_time))

# End of code
