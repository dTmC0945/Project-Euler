import numpy as np
from fractions import Fraction

def continuedFraction(n, d):
    """Return the terms of the continued fraction when n is the numerator
and d the divisor as a list"""
    if d == 0: return []         # Ok it is finished
    q = n//d                     # compute the integer quotient
    r = n - q*d                  # the rest
    return [q] + continuedFraction(d, r)        # and recurse...

print(Fraction(np.sqrt(23)))

print(continuedFraction(np.sqrt(23), 10))