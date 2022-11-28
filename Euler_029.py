
array = []

for a in range(2, 101):
    for b in range(2, 101):
        array.append(pow(a, b))


lsRemDup = len(list(set(array)))



print(lsRemDup)