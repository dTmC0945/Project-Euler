import numpy as np
import time

start_time = time.time()


def primeFinder(n):
    for div in range(2, int(np.sqrt(n)) + 1):
        if n % div == 0 and n != div:
            return 0

    return n


looper = 999999999

while looper > 100000000:
    prime = primeFinder(looper)
    if prime != 0:
        intArray = [char for char in str(prime)]
        if len(intArray) == len(set(intArray)):
            print(prime)
            looper -= 2
        else:
            looper -= 2
            continue

    else:
        looper -= 2
        continue

print("--- %s seconds ---" % (time.time() - start_time))
