import numpy as np  # for arrays and stuff
import time  # import for time calculation

start_time = time.time()  # start the clock

# open the textfile
with open('Euler_011.txt') as file:
    lines = file.readlines()

# remove the \n
mappedLines = list(map(lambda s: s.strip(), lines))

# convert the number list to integers and a 2D array
index = 0
array = np.zeros([20, 20])
for text in mappedLines:
    array[index] = list(map(int, text.split(" ")))
    index += 1

maximum = 0  # define the initial maximum value

# 1st case is up and down
for a in range(0, 16):
    for b in range(0, 20):
        updown = array[a + 0][b] * array[a + 1][b] * array[a + 2][b] * array[a + 3][b]
        if updown > maximum:
            maximum = updown

# 2nd case is left and right
for a in range(0, 20):
    for b in range(0, 16):
        leftright = array[a][b + 0] * array[a][b + 1] * array[a][b + 2] * array[a][b + 3]
        if leftright > maximum:
            maximum = leftright

# 3rd case is left diagonal
for a in range(0, 16):
    for b in range(0, 16):
        leftdiag = array[a + 0][b + 0] * array[a + 1][b + 1] * array[a + 2][b + 2] * array[a + 3][b + 3]
        if leftdiag > maximum:
            maximum = leftdiag

# 4th case is right diagonal
for a in range(0, 16):
    for b in range(0, 16):
        rightdiag = array[a + 3][b + 0] * array[a + 2][b + 1] * array[a + 1][b + 2] * array[a + 0][b + 3]
        if rightdiag > maximum:
            maximum = rightdiag

print(int(maximum))
print("--- %s seconds ---" % (time.time() - start_time))
