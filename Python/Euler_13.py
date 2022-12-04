# open the textfile
with open('Text Files/Euler_13.txt') as file:
    lines = file.readlines()

# remove the \n from each line
mappedLines = list(map(lambda s: s.strip(), lines))

# get the first eleven digits of each number
firstTen = [x[0:11] for x in mappedLines]

# convert the string values to integers
intLines = list(map(int, firstTen))

# output the sum of the values
output = str(sum([x for x in intLines]))

# print out the ten digits
tendigits = print(output[0:10])
