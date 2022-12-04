# Project Euler Question 1 - Multiples of 3 or 5

import numpy as np  # import for absolute function
import time  # import for time calculation

start_time = time.time()  # start the clock

# Average solve time (M1 Mac) - 0.60 sec

number = 2000000
value = 0
diff = 50000
for n in range(1, 1000):
    for m in range(1, 1000):
        answer = n * (n + 1) * m * (m + 1) / 4
        if np.abs(answer - number) < diff:
            diff = answer - number
            result = m * n


print("The sum of all the multiples of 3 or 5 below 1000 is:", result)
print("--- %s seconds ---" % (time.time() - start_time))