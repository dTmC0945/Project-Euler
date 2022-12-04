# Project Euler Question 9 - Special Pythagorean triplet

import numpy as np  # For sqrt function
import time  # import for time calculation

start_time = time.time()  # start the clock

# Average solve time (M1 Mac) - 1.82 sec

# Given the question is solved under 2 seconds, brute force method is used.

answer = []  # initialise empty array
for a in range(1, 1000):  # Checks for a values from 1 to 1000
    for b in range(1, 1000):  # Checks for values from 1 to 1000
        c = np.sqrt(pow(a, 2) + pow(b, 2))  # Calculate the triplet
        if c.is_integer() and c + a + b == 1000:  # Check if the calculated number is an integer
            answer.append(a)  # record the values for a
            answer.append(b)  # record the values for b
            answer.append(c)  # record the values for c
            answer.append(a * b * c)  # record the values for a * b * c
            break  # break the loop

# Print the results
print("The triplet is: a =", answer[0], ", b =", answer[1], "and c =", int(answer[2]))
print("The solution in: a * b * c = ", int(answer[-1]))
print("--- %s seconds ---" % (time.time() - start_time))

# End of code
