from mpmath import mp
mp.dps = 100

# Set the precision required by the question

array = []

for value in range(2, 101):
    square_Root = list(str(mp.sqrt(value)))
    print(square_Root)

    if "." not in square_Root:
        continue
    array.append(sum(list(map(int, (square_Root[square_Root.index(".") + 1:])))))

print(sum(array))