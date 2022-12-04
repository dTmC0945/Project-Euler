
import numpy as np

number = 2000000
value = 0
diff = 50
for n in range(1, 1000):
    for m in range(1, 1000):
        answer = n * (n + 1) * m * (m + 1) / 4
        if np.absolute(answer - number) < diff:
            diff = answer - number
            print(m * n, answer)


