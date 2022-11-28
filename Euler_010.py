import numpy as np


def sievePrime(n):
    array = np.arange(2, n)

    tempSieve = [2]

    for value in range(2, int(np.floor(np.sqrt(n)))):
        if tempSieve[value - 2] != value:
            continue
        else:
            for x in range(len(array)):
                if array[x] % value == 0 and array[x] != value:
                    array[x] = 0
                    tempSieve = array


    #tempSieve = array[array != 0]

    return sum(array)


print(sievePrime(1000000))
