
with open('Euler_13.txt') as file:
    lines = file.readlines()

mappedLines = list(map(lambda s: s.strip(), lines))

firstTen = [x[0:11] for x in mappedLines]

intLines = list(map(int, firstTen))

output = str(sum([x for x in intLines]))

tendigits = print(output[0:10])
