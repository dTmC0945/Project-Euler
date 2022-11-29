import numpy as np
import time

start_time = time.time()


def primeFinder(n):
    for div in range(2, int(np.sqrt(n))):
        if n % div == 0 and n != 0:
            break
        else:
            return n


print("--- %s seconds ---" % (time.time() - start_time))
