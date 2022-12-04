# Project Euler Question 8 - Largest product in a series

from functools import reduce # for the lambda product function
import numpy as np #import of the zeros array
import time  # import for time calculation

start_time = time.time()  # start the clock

# Average solve time (M1 Mac) - 0.0001 sec

# open the textfile
with open('Text Files/Euler_008.txt') as file:
    lines = file.readlines()

# remove the \n from each line
mappedLines = list(map(lambda s: s.strip(), lines))

p = []

for ls in mappedLines:
    p.append(list(ls))

collapse = sum(p, [])  # collapsing of matrix

number = 13

window = np.zeros(number)
size = len(window)

maxValue = 0
for a in range(len(collapse) - size):
    for b in range(size):
        window[b] = collapse[a + b]

    intWin = list(map(int, window))

    mult = reduce(lambda x, y: x * y, intWin)

    if mult > maxValue:
        maxValue = mult


print("The largest product of the %s digits is: %s" %(number, maxValue))
print("--- %s seconds ---" % (time.time() - start_time))

# End of code