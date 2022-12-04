# Project Euler Question 8 - Largest product in a series

from functools import reduce  # for the lambda product function
import numpy as np  # import of the zeros array
import time  # import for time calculation

start_time = time.time()  # start the clock

# Average solve time (M1 Mac) - 0.006 sec

# open the textfile
with open('Text Files/Euler_008.txt') as file:
    lines = file.readlines()

# remove the \n from each line
mappedLines = list(map(lambda s: s.strip(), lines))

p = []  # create an empty array to put the list into a single array

# put the values read to the array
for ls in mappedLines:
    p.append(list(ls))

collapse = sum(p, [])  # collapsing of matrix from 2D to 1D

number = 13  # number of digits given in the question

# create an empty array for the window that traverses the list p.
window = np.zeros(number)

maxValue = 0  # initial maximum value for the digit products

# moves the window each iteration and takes in the values.
for a in range(len(collapse) - number):
    for b in range(number):
        window[b] = collapse[a + b]

    intWin = list(map(int, window))

    # multiplies the values using lambda reduce function
    mult = reduce(lambda x, y: x * y, intWin)

    # if the multiplication is bigger save it a maxValue
    if mult > maxValue:
        maxValue = mult

print("The largest product of the %s digits is: %s" % (number, maxValue))
print("--- %s seconds ---" % (time.time() - start_time))

# End of code
