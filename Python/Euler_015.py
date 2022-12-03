# Project Euler Question 1 - Lattice Paths

import time  # import for time calculation

start_time = time.time()  # start the clock


# Average solve time (M1 Mac) - 0.000024 sec

# Define the factorial function (tried avoiding recursion for speed purposes)
def factorial(n):
    p = 1  # first factorial number (n0 = 1)
    i = 2  # second factorial number (n1 = 1)
    while i <= n:
        p *= i  # while loop is true multiply the p with the previous value
        i += 1  # increase the value
    return p


# The lattice questions is really a pascal triangle in disguise. To solve it you need to get the number
# of the grid size double it and find the max value of that values binomial distribution.
def binomialDist(n, k):
    # returns the binomial distribution of the values n and k.
    return factorial(n) / (factorial(k) * factorial(n - k))


grid_Number = 20

answer = binomialDist(grid_Number * 2, grid_Number)

print("There are", int(answer), " routes in a", grid_Number, "by", grid_Number, "grid")
print("--- %s seconds ---" % (time.time() - start_time))

# End of code
