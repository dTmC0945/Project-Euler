import math as m


def primeFinder(n):
    out = 0
    for i in range(2, m.floor(n / 2)):
        if n % i == 0 or n == 4:
            out = 0
            return 0

    if out == 0:
        return n

def primeUnder(n):

    array = [primeFinder(i) for i in range(2, n)]

    return sum(array)


print(primeUnder(20000))