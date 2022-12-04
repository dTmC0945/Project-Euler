# Project Euler Question 44 - Pentagon Numbers

import time  # import for time calculation

start_time = time.time()  # start the clock


# Average solve time (M1 Mac) - 0.05 sec

# Function to calculate the pentagonal numbers
def pentagonalNumber(number):
    return number * (3 * number - 1) / 2


array = [pentagonalNumber(number) for number in range(1, 1000)]


