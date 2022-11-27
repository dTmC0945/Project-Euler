
with open('Euler_13.txt') as file:
    lines = file.readlines()

lines = list(map(lambda s: s.strip(), lines))

print(lines)