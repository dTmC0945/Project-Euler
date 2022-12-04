# Project Euler Question 45 - Triangular, pentagonal and hexagonal

import time  # import for time calculation

start_time = time.time()  # start the clock


# Average solve time (M1 Mac) - 0.05 sec

# Function to calculate the triangle numbers
def triangleNumber(number):
    return number * (number + 1) / 2


# Function to calculate the pentagonal numbers
def pentagonalNumber(number):
    return number * (3 * number - 1) / 2


# Set initial values
number5, number6 = 165, 144

# The trick here is that triangle numbers and hexagonal number are equal when H(n) = T(2n -1)
# This loop just checks if triangle is equal to pentagonal and if not increase the smaller one to find it.
# If found it breaks the while true loop.

while True:
    if pentagonalNumber(number5) == triangleNumber(2 * number6 - 1):
        break
    elif pentagonalNumber(number5) > triangleNumber(2 * number6 - 1):
        number6 += 1
    elif pentagonalNumber(number5) < triangleNumber(2 * number6 - 1):
        number5 += 1

print("The next number is: ", int(pentagonalNumber(number5)))
print("--- %s seconds ---" % (time.time() - start_time))

# End of code
