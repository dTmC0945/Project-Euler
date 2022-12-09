from fractions import Fraction
import sys
from decimal import *
import numpy as np
getcontext().prec = 500

sys.setrecursionlimit(10000)

def digitCounter(number):
    return len(list(str(number)))


def f(x, max_depth):
    if x == max_depth:
        return 0
    else:
        return 1 / (2 + f(x + 1, max_depth))

count = 0

for depth in range(1,101):
    sqrt2 = 1 + f(1, depth)

    numerator = Fraction(sqrt2).limit_denominator().numerator
    denominator = Fraction(sqrt2).limit_denominator().denominator
    print(Decimal(sqrt2))
    if digitCounter(numerator) > digitCounter(denominator):
        count += 1
    else:
        continue

print(count)