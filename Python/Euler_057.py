from fractions import Fraction
import numpy as np
from math import gcd


def digitCounter(number):
    return len(list(str(number)))


def f(x, max_depth):
    if x == max_depth:
        return 0
    else:
        return 1 / (2 + f(x + 1, max_depth))

count = 0

for depth in range(1,1001):
    sqrt2 = 1 + f(1, depth)

    numerator = Fraction(sqrt2).limit_denominator().numerator
    denominator = Fraction(sqrt2).limit_denominator().denominator

    if digitCounter(numerator) > digitCounter(denominator):
        count += 1
    else:
        continue

print(count)