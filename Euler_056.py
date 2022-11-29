def digits(n):
    return sum(list(map(int, list(str(n)))))

max = 0
for a in range (1,100):
    for b in range(1,100):
        value = digits(a ** b)
        if value > max:
            max = value

print(max)