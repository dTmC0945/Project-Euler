import numpy as np  # import for arrays
import time  # import for time calculation

start_time = time.time()  # start the clock


def sievePrime(n):
    numberlist = np.arange(2, n)  # generate the number list from 2 to number n

    temp_sieve = [2]  # create the temporary sieve (starts with 2 and grows ... )

    for value in range(2, int(np.ceil(np.sqrt(n)))):  # check till sqrt(n) [saves time immensely]
        if temp_sieve[value - 2] != value:
            continue
        else:
            for x in range(value, len(range(n)), value):  # check the values from beginning of the prime
                # saves more time...
                if numberlist[x - 2] % value == 0 and numberlist[x - 2] != value:
                    numberlist[x - 2] = 0
                    temp_sieve = numberlist
                else:
                    continue

    return numberlist


# checks whether a given number is prime
def primeFinder(n):
    for div in range(2, int(np.ceil(np.sqrt(n)))):
        if n % div == 0 and n != div:
            return 0

    return n


# limit given in question
limit = 100000

# gather the array full of primes and removing the numbers
primeList = sievePrime(limit)[sievePrime(limit) != 0]

# initial sum of the primes (start with 2)
total = primeList[0]

for window in range(len(primeList), 1, -1):  # creates a window to sum up consecutive primes
    for ind in range(1, len(primeList) - window):  # the indices
        cache = sum(primeList[ind:ind + window])  # sums them up
        if cache >= limit:  # checks if the value is bigger then limit
            break  # if so terminate the loop
        elif primeFinder(cache) != 0:  # else check if it is primes
            print(cache)  # if so print it out
            break  # break

print("--- %s seconds ---" % (time.time() - start_time))
