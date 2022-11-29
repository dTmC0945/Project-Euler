def numberLength(n):
    return len(list(map(int, list(str(n)))))

number_List = []

for number in range(1,1000):
    for power in range(1, 100):
        if numberLength(number ** power) == power:
            number_List.append(number ** power)

print(len(number_List))