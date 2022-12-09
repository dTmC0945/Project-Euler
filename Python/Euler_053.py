# Project Euler Question 20 - Factorial Digit Sum

import time  # import for time calculation

start_time = time.time()  # start the clock


# Average solve time (M1 Mac) - 0.0001 sec

# factorial function
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)