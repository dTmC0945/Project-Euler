

def squareDigitNumber(n):
    digits = list(str(n))
    int_digits = list(map(int, digits))

    return sum(map(lambda x: x**2, int_digits))


n = 0

for num in range(1, 10000000):
    while num != 1 or num != 89:
        num = squareDigitNumber(num)
        if num == 89:
            n += 1
            break
        if num == 1:
            break

print(n)