import numpy as np


def perfectSquare(limit):
    array = []
    for value in range(2, int(np.ceil(np.sqrt(limit)))):
        array.append(value ** 2)

    return array


p_squares = perfectSquare(1000)

list = np.arange(2, 1000)

filtered_list = set(list) - set(p_squares)
max_x = 0
max_Value = 0
y = 1
for D in filtered_list:

    eq = np.sqrt(1 + D * y ** 2)
    while True:
        if eq.is_integer():
            print(D, eq)
            break

    if eq > max_x:
        max_x = eq
        max_Value = D

print(max_Value, max_x)
