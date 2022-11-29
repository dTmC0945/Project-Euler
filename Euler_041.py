import numpy as np
import time

start_time = time.time()


def primeFinder(n):
    for div in range(2, int(np.sqrt(n)) + 1):
        if n % div == 0 and n != div:
            return 0

    return n


looper = 9999999

while looper > 10**6:
    intArray = [char for char in str(looper)]
    if len(intArray) == len(set(intArray)) and primeFinder(looper) != 0:
        print(looper)
        looper -= 2
        break
    else:
        looper -= 2
        pass



print("--- %s seconds ---" % (time.time() - start_time))
