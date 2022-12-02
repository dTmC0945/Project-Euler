import numpy as np
import time

start_time = time.time()


# Sieve of Eratosthenes implementation
def sievePrime(n):
    array = np.arange(2, n)  # define the array of numbers up to the limit n

    temp_sieve = [2]  # declare a temporary sieve that retains the primes. Starts with 2.

    for value in range(2, int(np.ceil(np.sqrt(n)))):  # only care the numbers upto sqrt of n for speed purposes.
        if temp_sieve[value - 2] != value:  # skips the value if the looping value divides itself (save around 1 sec)
            continue
        else:
            for x in range(value, len(range(n)), value):  # loops the multiplies of the prime numbers to increase speed.
                if array[x - 2] % value == 0 and array[x - 2] != value:  # check if number divides with a number.
                    array[x - 2] = 0  # as it is not prime, change its values as 0
                    temp_sieve = array
                else:
                    continue

    return array  # returns the sieve as output.


def filter(array):
    input = array.sort()
    char_List = []
    for ind in range(0, len(input)):
        char_List.append(ord(input[ind]))

    return print(char_List)


prime_list = sievePrime(7654321)

prime_list = prime_list[prime_list != 0]

print(prime_list)

for prime in range(0, len(prime_list)):
    intArray = list(str(prime_list[prime]))
    if len(intArray) == 4 or len(intArray) == 7:
        if "0" not in intArray and len(intArray) == len(set(intArray)):
            filter(intArray)
            print(intArray)
    else:
        continue

# while looper > 10 ** 8:
#     intArray = [char for char in str(looper)]
#     if 0 in intArray:
#         break
#     else:
#         if len(intArray) == len(set(intArray)) and primeFinder(looper) != 0:
#             looper -= 2
#             break
#         else:
#             looper -= 2
#             pass
#
# print(looper)
print("--- %s seconds ---" % (time.time() - start_time))
