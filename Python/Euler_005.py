import numpy as np  # import for np arrays
import time  # import for time calculation
from functools import reduce  # import for lambda calculations

start_time = time.time()  # start the clock


# use the sieve of eratosthenes to calculate primes under n
def sievePrime(n):
    numberlist = np.arange(2, n)  # generate the number list from 2 to number n

    temp_sieve = [2]  # create the temporary sieve (starts with 2 and grows ... )

    for value in range(2, int(np.ceil(np.sqrt(n)))):  # check till sqrt(n) [saves time immensely]
        if temp_sieve[value - 2] != value:
            continue
        else:
            for x in range(value, len(range(n)), value):  # check the values from beginning of the prime
                # saves more time...
                if numberlist[x - 2] % value == 0 and numberlist[x - 2] != value:
                    numberlist[x - 2] = 0
                    temp_sieve = numberlist
                else:
                    continue

    return numberlist


# produces a list of numbers that divides up to nmax. Every division counts as one in array.
def divisor(n, nmax):
    array = np.zeros(nmax)  # generate a zero array size of nmax
    # counts how many times a number, divides a number (i.e., 16 would be divisible by 2 4 times)
    for div in range(2, n + 1):
        upper = n
        while upper > 1:
            if upper % div == 0:
                array[div - 1] += 1
                upper = upper / div
            else:
                break

    return array

limit = 20

# generate a 2D matrix of each number divisible by each other number up to a certain number
power = np.asarray([divisor(n, limit) for n in range(1, limit + 1)])
# find the maximum of each column
max = power.max(axis=0, keepdims=True)
# find prime numbers up to a certain value
prime = np.insert(sievePrime(limit + 1), 0, [0])

index = 0
total = []

# take the power of each number with its corresponding prime value
for number in range(0, limit):
    index = 0
    if prime[number] != 0:
        cache = pow(prime[number], max[0][number])
        total.append(cache)

print(total)
# multiply all the values of the array
mult = reduce(lambda x, y: x * y, total)

print("The smallest number divisible by %s is: %s" % (limit, int(mult)))
print("--- %s seconds ---" % (time.time() - start_time))
