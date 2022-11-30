from fractions import Fraction


def fractionalSum(number, array):
    if number == 0:
        return array[0]
    elif number == 1:
        return array[0] + Fraction(1, array[1])
    else:
        return array[number] + Fraction(1, array[number] + fractionalSum(number - 1, array))



expansion = [2, 1]
it = 1
clock = 0
for i in range(1,110):
    if clock == 0:
        expansion.append(2*it)
        it += 1
        clock = 2
    if clock != 0:
        expansion.append(1)
        clock -= 1

print(fractionalSum(1, expansion))
