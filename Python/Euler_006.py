# Project Euler Question 6 - Sum Square Difference

import time  # import for time calculation

start_time = time.time()  # start the clock

# Average solve time (M1 Mac) - 0.00006 sec


def sumSquare(n):
    return sum(map(lambda x: pow(x, 2), range(n + 1)))


def squareSum(n):
    return pow(sum(map(lambda x: x, range(n + 1))), 2)


number = 100 # number given in question.

difference = squareSum(number) - sumSquare(number)

print("The Difference of first %s is: %s" % (number, difference))
print("--- %s seconds ---" % (time.time() - start_time))

# End of code
