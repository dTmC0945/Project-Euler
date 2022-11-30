# Project Euler Question 40 - Champernowne's constant

import numpy as np  # import for ceiling function
import time  # import for time calculation

start_time = time.time()  # start the clock

# Average solve time (M1 Mac) - 0.05 sec


# function calculating the champernowne digits.
def ChampernowneDigits(n):
    digits = "0"  # initial place to store the digits. 0 is added to make array look pleasant.
    for digit in range(1, n + 1):
        digits += str(digit)  # add the digits as string to the digits value.
    return digits


# Calculation of the upper bound
upper_bound = int(np.ceil((1000000 - 9 * 1 - 90 * 2 - 900 * 3 - 9000 * 4 - 90000 * 5) / 6))

# Set the upper limit on the function and state it to get the 1.000.000 digits. Explained in theory
one_million = ChampernowneDigits(100000 + upper_bound)

# Get the 1st digit
d1 = int(one_million[1])

# Get the 10th digit
d10 = int(one_million[10])

# Get the 100th digit
d100 = int(one_million[100])

# Get the 1.000th digit
d1000 = int(one_million[1000])

# Get the 10.000th digit
d10000 = int(one_million[10000])

# Get the 100.000th digit
d100000 = int(one_million[100000])

# Get the 1.000.000th digit
d1000000 = int(one_million[1000000])

# Finally multiply the value to get the solution
solution = d1 * d10 * d100 * d1000 * d10000 * d100000 * d1000000

print(solution)

print("--- %s seconds ---" % (time.time() - start_time))

# End of code

# Theory

# The major challenge is to find the upper limit. While this can be done by using a while loop,
# you can also calculate it by hand. As we need 1.000.000 digits we know that there are,
# 9 digits only having 1 digits,
# 90 digits having 2 digits,
# 900 digits having 3 digits,
# 9.000 digits having 4 digits,
# 90.000 digits having 5 digits,
# 900.000 digits having 6 digits
# For this question we only need 1.000.000 digits so, we need to solve the following equation
# 1.000.000 = 9 * 1 + 90 * 2 + 900 * 3 + 9.000 * 4 + 90.000 * 5 + n * 6
# Solve this and, you will get 85186 with np.ceil. Then you need to add 100000 to take all the other preeceding
# digits into account.
