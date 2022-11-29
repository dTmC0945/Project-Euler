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


power = np.asarray([divisor(n, 20) for n in range(1, 21)])
max = power.max(axis=0, keepdims=True)

prime = np.insert(sievePrime(21), 0, [0])

total = 0
index = 0

print(prime)
print(max)
total = []

for value in range(0, 20):
    index = 0
    if prime[value] != 0:
        cache = pow(prime[value], max[0][value])
        total.append(cache)

mult = reduce(lambda x, y: x * y, total)

print(mult)
print("--- %s seconds ---" % (time.time() - start_time))
