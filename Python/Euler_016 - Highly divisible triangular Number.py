# Project Euler Question 12 - Highly divisible triangular Number

import time  # import for time calculation

start_time = time.time()  # start the clock

# Average solve time (M1 Mac) - 0.00005 sec

number = 1000  # Number given in the question

# convert the number to string
digit_list = list(str(pow(2, number)))

# convert the list of strings to int
digit_int = list(map(int, digit_list))

# sum of the digits
answer = sum(digit_int)

print("The sum of the digits of the number 2**1000 is: ", answer)
print("--- %s seconds ---" % (time.time() - start_time))

# End of code
