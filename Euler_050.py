import numpy as np  # import for arrays
import time  # import for time calculation

start_time = time.time()  # start the clock


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


def primeFinder(n):
    for div in range(2, int(np.sqrt(n)) + 1):
        if n % div == 0 and n != div:
            return 0

    return n

limit = 1000

primeList = sievePrime(limit)[sievePrime(limit) != 0]


total = primeList[0]
for ind in range(1, len(primeList)):
    cache = sum(primeList[0:ind])
    if cache < 1000:
        if primeFinder(cache) != 0:
            print(cache)

    else:
        break