# Project Euler Question 41 - Pan digital Prime

import numpy as np  # numpy for array, sqrt and ceil
import time  # import for time calculation

start_time = time.time()  # start the clock


# Average solve time (M1 Mac) - 5.6 sec


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


# Number filter to filter out numbers that are not 1 to n
def filteredPrime(array):
    # Sort out those pesky integers
    sorted_int = sorted(array)

    # Loop through each int list.
    for ind in range(0, len(sorted_int) - 1):

        # Check if each preceding number is 1 bigger than the other. If not return 0
        if sorted_int[ind + 1] - sorted_int[ind] != 1:
            return 0

    # As the question states 1 to n it must include 1.
    if 1 not in sorted_int:
        return 0
    else:
        return array # else return the array


# we only need to check numbers that are 4 digits or 7 digits.
prime_list = sievePrime(7654321)

max_prime = 0
# remove the zeroes
prime_list = prime_list[prime_list != 0]

# main checking place ...
for prime in range(0, len(prime_list)):

    # turn the prime number into a list of string.
    intArray = list(str(prime_list[prime]))

    # check if contains 4 digits or 7 digits
    if len(intArray) == 4 or len(intArray) == 7:

        # make sure 0 is not in array and filteredPrime function does not return 0.
        if "0" not in intArray and filteredPrime(list(map(int, intArray))) != 0:
            max_prime = prime_list[prime]

    else:
        continue

print("The biggest pan digital number is: %s" % max_prime)
print("--- %s seconds ---" % (time.time() - start_time))

# End of code