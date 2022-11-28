
# open the textfile
with open('Euler_8.txt') as file:
    lines = file.readlines()

# remove the \n from each line
mappedLines = list(map(lambda s: s.strip(), lines))

p = []

for x in mappedLines:
    p.append(list(x))

collapse = sum(p, []) # collapsing of matrix