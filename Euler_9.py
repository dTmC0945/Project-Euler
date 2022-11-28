import numpy as np

for a in range(1, 1000):
    for b in range(1, 1000):
        c = np.sqrt(pow(a, 2) + pow(b, 2))
        if c.is_integer() and c + a + b == 1000:
            print(a*b*c)

