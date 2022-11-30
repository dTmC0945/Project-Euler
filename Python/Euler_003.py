# Project Euler Question 3 - Largest Prime Factor

import numpy as np
import time  # import for time calculation

start_time = time.time()  # start the clock

# Average solve time (M1 Mac) - 0.72 sec


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


number = 600851475143  # number given in the question

primeList = sievePrime(int(np.ceil(np.sqrt(number))))  # generate the primelist from
# the sieve function up to the sqrt of the number to increase the speed

primeList = primeList[primeList != 0]  # remove the zeroes from the sieve array

max_prime = 0  # define a variable to store the maximum prime number

for index in primeList:
    if number % index == 0:  # if the prime divides the number store it.
        max_prime = index

print("The largest prime factor of the number 600851475143 is:", max_prime)

print("--- %s seconds ---" % (time.time() - start_time))

# End of code
