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

total = 0

for x in intValues:
    print(x)
    total = total + x

print(total)
