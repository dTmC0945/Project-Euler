# Project Euler Question 20 - Factorial Digit Sum

import time  # import for time calculation

start_time = time.time()  # start the clock


# Average solve time (M1 Mac) - 0.000024 sec

# factorial function
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)


# mapping the number into string characters
mappedLines = list(map(lambda s: s.strip(), str(factorial(100))))

# convert the string to integers
intValues = list(map(int, mappedLines))

total = 0  # initialise the empty value to store the sum

for x in intValues:
    total = total + x

print("The sum of the digits in the number 100 is:", total)
print("--- %s seconds ---" % (time.time() - start_time))

# End of code
