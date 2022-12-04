# Project Euler Question 24 - Lexicographic permutations

import time  # import for time calculation
import itertools  # import for permutations system function

start_time = time.time()  # start the clock

# Average solve time (M1 Mac) - 0.45 sec

# There is a system function which calculates the permutation list so why not :) ?
answer = list(itertools.permutations([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))[999999]

print("The 1000000th permutation is: ", answer)
print("--- %s seconds ---" % (time.time() - start_time))

# End of code
