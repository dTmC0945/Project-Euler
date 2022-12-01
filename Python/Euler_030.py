# Project Euler Question 1 - Digit fifth powers

import time  # import for time calculation

start_time = time.time()  # start the clock


# Average solve time (M1 Mac) - 1.1 sec

# Calculates the sum of the digits with a given power
def powerDigitSum(n, superscript):
    # Convert the digits first into str, separates them and produces a list of integers
    digits = list(map(int, list(str(n))))

    # Sums them up using lambda function
    digit_sum = sum(map(lambda x: pow(x, superscript), digits))

    # Returns the number that matches otherwise returns 0.
    if digit_sum == n:
        return digit_sum
    else:
        return 0


number = 5  # number given in question

# Produces the sum
total = sum(map(lambda x: powerDigitSum(x, number), range(2, 354295)))

print("The sum of numbers that can be written as the digit sum of powers of %s is: %s" % (number, int(total)))
print("--- %s seconds ---" % (time.time() - start_time))

# End of code
