# Project Euler Question 36 - Double-base Palindromes

import time  # import for time calculation

start_time = time.time()  # start the clock


# Average solve time (M1 Mac) - 1 sec


# Checks if a number is palindrome
def palindromeChecker(number):
    n_dec = number  # value in decimal
    n_bin = int(bin(n_dec)[2:])  # value in binary

    text_dec = str(n_dec)  # convert it into a string
    text_bin = str(n_bin)  # convert it into a string

    reverse_dec = text_dec[::-1]  # reverse the string
    reverse_bin = text_bin[::-1]  # reverse the string

    # check if the number is a palindrome
    if text_dec == reverse_dec and text_bin == reverse_bin:
        return number
    else:
        return 0


total = 0
for value in range(1, 1000000):
    total = palindromeChecker(value) + total

print("The sum is:", total)
print("--- %s seconds ---" % (time.time() - start_time))

# End of code
