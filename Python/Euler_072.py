# Project Euler Question 72 - Counting Fractions

from functools import lru_cache
import numpy as np  # import for np arrays and ceiling function
import time  # import for time calculation
import math

start_time = time.time()  # start the clock


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


# Calculates primes up to 1000000 as given in question
prime_list = sievePrime(1000000)

prime_list = prime_list[prime_list != 0]

# Calculates the euler Totient Function
def eulerTotient(array, value):
    temporary = []
    for ind in range(0, len(prime_list)):
        if value == prime_list[ind]:
            return value - 1
        elif value > prime_list[ind]:
            if value % prime_list[ind] == 0:
                temporary.append(1 - 1 / prime_list[ind])
        else:
            break
    return int(value * math.prod(temporary))


answer = sum(map(lambda x: eulerTotient(prime_list, x), range(2, 100)))

print(answer)

print("--- %s seconds ---" % (time.time() - start_time))

# End of code