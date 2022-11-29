import numpy as np
import time
from functools import reduce

start_time = time.time()


def sievePrime(n):
    array = np.arange(2, n)

    tempsieve = [2]

    for value in range(2, int(np.floor(np.sqrt(n)))):
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


def divisor(n, nmax):
    array = np.zeros(nmax)

    for div in range(2, n + 1):
        upper = n
        while upper > 1:
            if upper % div == 0:
                array[div - 1] += 1
                upper = upper / div
            else:
                break

    return array


power = [divisor(n, 20) for n in range(1, 20)]

prime = np.insert(sievePrime(21), 0, [0, 0])

print(prime)


print("--- %s seconds ---" % (time.time() - start_time))
