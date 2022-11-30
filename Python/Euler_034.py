def digitiser(n):
    return list(map(int, list(str(n))))


def factorial(n):
    iterator = 1
    case = 2
    while case <= n:

        iterator = iterator * case
        case += 1
    return iterator


for n in range(3, 1000000):
    digits = digitiser(n)

    total = 0
    for dig in digits:
        total = factorial(dig) + total

    if total == n:
        print(n)

print(40585 + 145)