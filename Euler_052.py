def digitChecker(n):
    return sorted(list(map(int, list(str(n)))))

p = 2
k = 11

while p <= 6:
    if digitChecker(k) == digitChecker(p * k):
        print(p, k)
        p += 1
    else:
        k += 1



