# Project Euler Question 72 - Counting Fractions

import functools
import numpy as np  # import for np arrays and ceiling function
import time  # import for time calculation

start_time = time.time()  # start the clock


# Average solve time (M1 Mac) - 1.56 sec

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


number = 1000000  # given number

# Calculates primes up to 1000000 as given in question
prime_list = sievePrime(number)

prime_list = prime_list[prime_list != 0]  # removes the unnecessary zeroes

int_list = np.arange(0, number + 1)  # create an integer list to sieve

# Here the loops basically traverses the integer list and multiplies by 1 - 1/p if it divides with it
for prime in prime_list:
    for i in range(0, len(int_list), prime):
        int_list[i] = int_list[i] * (1 - 1 / prime)

print(sum(int_list) - 1)  # remove the phi(1) as it is not counted towards the question.
print("--- %s seconds ---" % (time.time() - start_time))

# # End of code
