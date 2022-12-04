# Project Euler Question 44 - Pentagon Numbers

import time  # import for time calculation

start_time = time.time()  # start the clock


# Average solve time (M1 Mac) - 0.05 sec

# Function to calculate the pentagonal numbers
def pentagonalNumber(number):
    return number * (3 * number - 1) / 2


array = [pentagonalNumber(number) for number in range(1, 10000)]

for ind in range(0, len(array)-1):
    for win in range(1, len(array) - ind):
        if array[ind] + array[ind + win] in set(array):
            print(array[ind], array[ind + win])

