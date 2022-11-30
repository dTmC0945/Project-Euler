import numpy as np
import time

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

    return sum(array)


print(sievePrime(2000000))
print("--- %s seconds ---" % (time.time() - start_time))
