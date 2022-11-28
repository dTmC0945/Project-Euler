import numpy as np


def numbersThatDivide(number):
    divisors = []
    for n in range(1, int(np.floor(number / 2)) + 1):
        if number % n == 0:
            divisors.append(n)

    return divisors


a, b = [], []

for value in range(1, 10000):
    if sum(numbersThatDivide(sum(numbersThatDivide(value)))) == value:
        a.append(value)
        b.append(sum(numbersThatDivide(value)))

valueSum =[]

print(a)
print(b)

for index in range(0, len(a)):
    if a[index] != b[index]:
        print(valueSum)
        valueSum.append(a[index] + b[index])
    else:
        continue

print(sum(list(set(valueSum))))