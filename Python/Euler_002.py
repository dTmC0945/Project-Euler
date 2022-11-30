# Project Euler Question 2 - Even Fibonacci Numbers

import time  # import for time calculation

start_time = time.time()  # start the clock


# Average solve time (M1 Mac) - 0.00005 sec

# Define the fibonacci function (tried avoiding recursion for speed purposes)
def fibonacci(n):
    p = 0  # first fibonacci numbers (F0)
    q = 1  # second fibonacci number (F1)
    for i in range(0, n):
        p, q = q, p + q  # as a tuple, assign F0 the value of F1 and F1 the value of F2 (i.e., F1 + F0)

    return p


limit, index, total = 0, 1, 0  # define the necessary variables
while limit < 4000000:  # if any fibonacci number is reached break the loop
    limit = fibonacci(index)
    if limit > 4000000:  # this is done to catch the final number that passes the limit before the while loop repeats
        break
    else:
        if limit % 2:
            total = limit + total

    index += 1

print("The sum of all even fibonacci numbers under 4.000.000 is:", total)

print("--- %s seconds ---" % (time.time() - start_time))

# End of code
