# Project Euler Question 5 - Smallest Multiple

import numpy as np  # import for np arrays and ceiling function
import time  # import for time calculation
from functools import reduce  # import for lambda calculations

start_time = time.time()  # start the clock

# Average solve time (M1 Mac) - 0.0003 sec


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


# produces a list of numbers that divides upper_bound.
# Every division counts as one in array. For example 16 is divided by 2 4 times so in place of 2
# 4 would be written. This will be used as the power values.
def divisor(n, upper_bound):
    array = np.zeros(upper_bound)  # generate a zero array size of upper_bound.
    # counts how many times a number, divides a number (i.e., 16 would be divisible by 2 4 times)
    for div in range(2, n + 1):
        upper = n  # set the number to be divided as upper
        while upper > 1:  # check if it is still bigger than 1
            if upper % div == 0:  # check if it divides without leftovers
                array[div - 1] += 1  # if it divides count this division in the correct place
                upper = upper / div  # update the number and check if it divides again.
            else:
                break

    return array


limit = 20  # number  given in question.

# generate a 2D matrix of each number divisible by each other number up to a certain number
power = np.asarray([divisor(n, limit) for n in range(1, limit + 1)])

# find the maximum of each column
maximum = power.max(axis=0, keepdims=True)

# find prime numbers up to a certain value
prime = np.insert(sievePrime(limit + 1), 0, [0])

total = []  # declare an empty array to find the prime numbers that divides limit.

# take the power of each number with its corresponding prime value
for number in range(0, limit):
    index = 0
    if prime[number] != 0:
        cache = pow(prime[number], maximum[0][number])
        total.append(cache)


# multiply all the values of the array
mult = reduce(lambda x, y: x * y, total)

print("The smallest number divisible by %s is: %s" % (limit, int(mult)))
print("--- %s seconds ---" % (time.time() - start_time))

# End of code
