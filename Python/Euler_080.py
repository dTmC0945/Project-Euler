from bigfloat import *
from decimal import *

# Set the precision required by the question
getcontext().prec = 150

array = []

for value in range(2, 101):
    square_Root = list(str(Decimal(value).sqrt()))
    if "." not in square_Root:
        print(value)
        continue
    array.append(sum(list(map(int, (square_Root[square_Root.index(".") + 1:square_Root.index(".") + 101])))))


print(sum(array))