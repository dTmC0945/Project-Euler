from functools import reduce
import numpy as np

# open the textfile
with open('Text Files/Euler_008.txt') as file:
    lines = file.readlines()

# remove the \n from each line
mappedLines = list(map(lambda s: s.strip(), lines))

p = []

for ls in mappedLines:
    p.append(list(ls))

collapse = sum(p, [])  # collapsing of matrix

window = np.zeros(13)
size = len(window)

maxValue = 0
for a in range(len(collapse) - size):
    for b in range(size):
        window[b] = collapse[a + b]

    intWin = list(map(int, window))

    mult = reduce(lambda x, y: x * y, intWin)

    if mult > maxValue:
        maxValue = mult

print(maxValue)
