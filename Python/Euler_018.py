# open the textfile
with open('Text Files/Euler_018.txt') as file:
    lines = file.readlines()

mappedLines = list(map(lambda s: s.strip(), lines))

for text in mappedLines:
    print(text.split())