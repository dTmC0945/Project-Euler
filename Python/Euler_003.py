# Project Euler Question 3 - Largest Prime Factor

import numpy as np
import time  # import for time calculation

start_time = time.time()  # start the clock


# Average solve time (M1 Mac) - 0.72 sec


def sievePrime(n):
    array = np.arange(2, n)

    tempsieve = [2]

    for value in range(2, int(np.ceil(np.sqrt(n)))):
        if tempsieve[value - 2] != value:
            continue
        else:
            for x in range(value, len(range(n)), value):
                if array[x - 2] % value == 0 and array[x - 2] != value:
                    array[x - 2] = 0
                    tempsieve = array
                else:
                    continue

    return array


number = 600851475143

primeList = sievePrime(int(np.ceil(np.sqrt(number))))

primeList = primeList[primeList != 0]

max_prime = 0

for index in primeList:
    if number % index == 0:
        max_prime = index

print("The largest prime factor of the number 600851475143 is:", max_prime)

print("--- %s seconds ---" % (time.time() - start_time))

# End of code
