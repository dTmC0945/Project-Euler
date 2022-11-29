import time  # import for time calculation

start_time = time.time()  # start the clock


def palindromeChecker(n):
    text_number = list(str(n))
    reverse = int(''.join(text_number[::-1]))

    return n, reverse


count = []

for initial in range(10, 10001):

    value = initial
    step = 0

    while step <= 50:
        init, reverse = palindromeChecker(initial)
        if init == reverse:
            break
        else:
            initial = init + reverse
            step += 1

    if step >= 50:
        count.append(value)

print(count)

print("--- %s seconds ---" % (time.time() - start_time))
