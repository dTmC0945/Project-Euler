# Project Euler Question 69 - Totient Maximum

import numpy as np
from math import gcd # importing built in gcd for speed
import time  # import for time calculation

start_time = time.time()  # start the clock


# Average solve time (M1 Mac) - 1.1 sec

# Sieve of Eratosthenes implementation
def sievePrime(n):
    array = np.arange(2, n)  # define the array of numbers up to the limit n

    temp_sieve = [2]  # declare a temporary sieve that retains the primes. Starts with 2.

    for value in range(2, int(np.ceil(np.sqrt(n)))):  # only care the numbers upto sqrt of n for speed purposes.
        if temp_sieve[value - 2] != value:  # skips the value if the looping value divides itself (save around 1 sec)
            continue
        else:
            for x in range(value, len(range(n)), value):  # loops the multiplies of the prime numbers to increase speed.
                if array[x - 2] % value == 0 and array[x - 2] != value:  # check if number divides with a number.
                    array[x - 2] = 0  # as it is not prime, change its values as 0
                    temp_sieve = array
                else:
                    continue

    return array  # returns the sieve as output.

print(len(sievePrime(1000000)[sievePrime(1000000) != 0]))

# Calculating euler Totient function
def eulerTotient(n):
    # returns the sum of the numbers that are co-prime with entered number n.
    return sum(map(lambda x: 1 if(gcd(n, x) == 1) else 0, range(1, n)))

# max_Value = 0
# max_Number = 0
# for number in range(2, 100000, 2):
#     if (number / eulerTotient(number)) > max_Value:
#         max_Value = number / eulerTotient(number)
#         max_Number = number
#     else:
#         continue


# print(max_Value, max_Number)
print("--- %s seconds ---" % (time.time() - start_time))

# End of code