# Project Euler Question 17 - Number letter counts

import inflect  # import for number to text converter
import time  # import for time calculation

start_time = time.time()  # start the clock

# Average solve time (M1 Mac) - 0.035 sec


p = inflect.engine()  # initiate the "inflect" module

count = []  # initialise the array to put the values

for number in range(1, 1001):
    # convert the number into text
    words = p.number_to_words(number)

    # remove special characters
    words_filtered = ''.join(char for char in words if char.isalnum())

    # append the values to an array
    count.append(len(words_filtered))

print("The sum is %s" % sum(count))
print("--- %s seconds ---" % (time.time() - start_time))

# End of Code
