
with open('Euler_13.txt') as file:
    lines = file.readlines()

lines = list(map(lambda s: s.strip(), lines))

intLines = list(map(int, lines))

print(intLines)

for x in intLines:

    Array = [x]


print(Array)