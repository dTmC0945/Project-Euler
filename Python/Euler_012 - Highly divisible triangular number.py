# Project Euler Question 12 - Highly divisible triangular Number

import numpy as np  # for arrays and stuff
import time  # import for time calculation

start_time = time.time()  # start the clock


# Average solve time (M1 Mac) - 2.7 sec


# Function to calculate the numbers that divide the given number
def numbersThatDivide(number):
    # create an empty array
    divisors = []
    for n in range(1, int(np.sqrt(number))):
        if number % n == 0:
            divisors.append(n)
            divisors.append(int(number / n))
    return divisors


# Calculate the triangle number sequence up to a given number n
def triangleNumber(number):
    return sum(range(1, number + 1))


# Declare the empty variables
div, value, answer = 0, 0, 0
limit = 500 # value given in the question

# Finds the triangle number that has more than 500 divisors
while div < limit:
    div = len(numbersThatDivide(triangleNumber(value)))
    answer = value
    value += 1

print(triangleNumber(answer))
print("--- %s seconds ---" % (time.time() - start_time))

# End of code