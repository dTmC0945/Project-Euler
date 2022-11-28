import numpy as np
import time

start_time = time.time()


def numbersThatDivide(number):
    divisors = []
    for n in range(1, int(np.sqrt(number))):
        if number % n == 0:
            divisors.append(n)
            divisors.append(int(number / n))

    return divisors


def triangleNumber(number):
    return sum(range(1, number + 1))


div, value = 0, 0

while div <= 400:
    div = len(numbersThatDivide(triangleNumber(value)))
    value += 1

print("--- %s seconds ---" % (time.time() - start_time))
