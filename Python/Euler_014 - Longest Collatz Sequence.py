# Project Euler Question 14 - Longest Collatz Sequence

import time  # import for time calculation

start_time = time.time()  # start the clock


# Average solve time (M1 Mac) - 15.3 sec


# The function that calculate the collatz chain
def Collatz(n):
    count = 1
    while n > 1:
        count += 1
        if n % 2 == 0:
            n /= 2
        else:
            n = 3 * n + 1
    return count


limit = 1000000  # limit given in the question
maxValue, maxCount = 0, 0  # setting the parameters

for number in range(1, limit):
    if Collatz(number) > maxCount:
        maxCount, maxValue = Collatz(number), number

print("The longest chain under %s is given by number %s" % (limit, maxValue))
print("--- %s seconds ---" % (time.time() - start_time))

# End of code
