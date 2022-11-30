from fractions import Fraction


def inside(index, place):
    if place >= 0:
        return Fraction(1, index + place)
    else:
        return Fraction(1, index)


def fractionalSum(number, array):
    if number == 0:
        return 0
    elif number == 1:
        return inside(array[0], 0)
    #elif number == 2:
    #    return inside(1, inside(array[2], 0))
    #elif number == 88:
       # return inside(array[1], inside(array[2], inside(array[3], inside(array[4], inside(array[5], 0)))))
    else:
        return inside(array[number-2], inside(array[number-1], 0))



# Fraction(1, array[1] + Fraction(1, array[2] + Fraction(1, array[3])))

expansion = [1]
it = 1
clock = 0
for i in range(1, 110):
    if clock == 0:
        expansion.append(2 * it)
        it += 1
        clock = 2
    if clock != 0:
        expansion.append(1)
        clock -= 1
print(expansion)
print(2 + fractionalSum(4, expansion))
