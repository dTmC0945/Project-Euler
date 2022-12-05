# Project Euler Question 13 - Large Sum

import time  # import for time calculation

start_time = time.time()  # start the clock

# Average solve time (M1 Mac) - 0.0003 sec

# open the textfile
with open('Text Files/Euler_013.txt') as file:
    lines = file.readlines()

# remove the \n from each line
mappedLines = list(map(lambda s: s.strip(), lines))

# get the first eleven digits of each number
firstTen = [x[0:11] for x in mappedLines]

# convert the string values to integers
intLines = list(map(int, firstTen))

# output the sum of the values
output = str(sum([x for x in intLines]))

# print out the ten digits
tendigits = output[0:10]

print("The first ten digits of the sum is:", tendigits)
print("--- %s seconds ---" % (time.time() - start_time))

# End of code
