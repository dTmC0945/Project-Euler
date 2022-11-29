import numpy as np


def powerSum(n):
    return pow(n, n)

print(sum((powerSum(n) for n in range(1, 1001))) % 10 ** 10)
