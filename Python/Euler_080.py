from bigfloat import *
from decimal import *
getcontext().prec = 100  # Change the precision

array = []

array.append(sum(list(map(int, list(str(Decimal(2).sqrt()))[2:])))))
