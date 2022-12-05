# Project Euler Question 4 - Largest Palindrome Product

import time  # import for time calculation

start_time = time.time()  # start the clock

# Average solve time (M1 Mac) - 0.4 sec


# Checks if a number is palindrome
def palindromeChecker(number1, number2):
    n = number1 * number2  # multiplies the numbers

    text = str(n)  # convert it into a string

    reverse = text[::-1]  # reverse the string

    # check if the number is a palindrome
    if text == reverse:
        return n
    else:
        return 0


bigValue = 0  # value assigned to keep only the biggest values

for a in range(99, 1000):  # checks all the 3-digit numbers for number a
    for b in range(99, 1000):  # checks all the 3-digit numbers for number b
        number = palindromeChecker(a, b)
        if number > bigValue:  # if the number is bigger than bigValue assign it as max.
            bigValue = number

print("The largest palindrome made from the product of two 3-digit numbers is:", bigValue)
print("--- %s seconds ---" % (time.time() - start_time))

# End of code
