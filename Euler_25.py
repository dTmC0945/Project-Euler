# avoid recursion, wrote it in while loop
def fibonacci(n):
    array = [1, 1]

    i = 2
    while i < n:
        array.append(array[i - 1] + array[i - 2])
        i += 1

    return array


length, n = 1, 3

while length < 1000:
    fib = fibonacci(n)
    length = len(str(fib[-1]))
    n += 1

print(n - 1)
