from fractions import Fraction


def fractionalSum(number, array):
    def inside(index, place):
        if place >= 0:
            return Fraction(1, index + place)
        else:
            return Fraction(1, index)

    if number == 0:
        return 0
    elif number == 1:
        return inside(array[number - 1], 0)
    elif number == 2:
        return inside(1, fractionalSum(number - 1, array))
    elif number == 88:
        return inside(array[0], inside(array[1], inside(array[2], inside(array[3], inside(array[4], 0)))))
    else:
        return inside(fractionalSum(number - 2, array), inside(fractionalSum(number - 1, array), 0))


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
print(2 + fractionalSum(3, expansion))
