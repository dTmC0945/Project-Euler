# Project Euler Question 26 - Reciprocal Cycles

from mpmath import *
import numpy as np  # import for arrays and ceiling function
import time  # import for time calculation
import re

start_time = time.time()  # start the clock

# Average solve time (M1 Mac) - 0.14 sec

mp.dps = 2000  # set precision to the question


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


# The only values that could possibly create repetitive patterns are prime numbers
prime_list = sievePrime(1000)  # Here is our good friend the sievePrime function

prime_list = prime_list[prime_list != 0]  # remove the zeroes from the sieve array

# A regular expression
r = re.compile(r"(.+?)\1+")
# . Matches any character except line breaks
# + Matches 1 or more of the preceding token
# ? Match as few characters as possible
# \1 Match the result

max_length, output = 0, 0 # define value for the loop

for prime in prime_list:

    # filter the numbers and give only the repetition
    repetition = r.findall(str(mpmathify("1/%s" % prime)))

    # some numbers will produce [] so we need to filter that out as well...
    if not repetition:
        continue
    else:
        # get the length of the repetition
        rep_length = len(max(repetition, key=len))
        if rep_length > max_length:
            max_length = rep_length
            output = prime
        else:
            continue


print("The number %s has the highest repetition with %s" %(output, max_length))
print("--- %s seconds ---" % (time.time() - start_time))

# End of Code
