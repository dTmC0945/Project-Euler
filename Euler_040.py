# Project Euler Question 40 - Champernowne's constant

import time  # import for time calculation

start_time = time.time()  # start the clock


# function calculating the champernowne digits.
def ChampernowneDigits(n):
    digits = "0"  # initial place to store the digits. 0 is added to make array look pleasant.
    for digit in range(1, n + 1):
        digits += str(digit)  # add the digits as string to the digits value.
    return digits


one_million = ChampernowneDigits(185186)

d1 = int(one_million[1])
d10 = int(one_million[10])
d100 = int(one_million[100])
d1000 = int(one_million[1000])
d10000 = int(one_million[10000])
d100000 = int(one_million[100000])
d1000000 = int(one_million[1000000])

solution = d1 * d10 * d100 * d1000 * d10000 * d100000 * d1000000

print(solution)

print("--- %s seconds ---" % (time.time() - start_time))

# End of code
