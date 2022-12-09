# Project Euler Question 20 - Factorial Digit Sum

import time  # import for time calculation

start_time = time.time()  # start the clock


# Average solve time (M1 Mac) - 0.0001 sec

# Define the factorial function (tried avoiding recursion for speed purposes)
def factorial(n):
    p = 1  # first factorial number (n0 = 1)
    i = 2  # second factorial number (n1 = 1)
    while i <= n:
        p *= i  # while loop is true multiply the p with the previous value
        i += 1  # increase the value
    return p

def binomial(n, r):
    return factorial(n) / (factorial(r) * factorial(n -r))

count = 0

for high in range(2, 101):
    for low in range(1, high):
        value = binomial(high, low)
        if value > 1000000:
            count += 1

print("There are")
print("--- %s seconds ---" % (time.time() - start_time))

# End of code