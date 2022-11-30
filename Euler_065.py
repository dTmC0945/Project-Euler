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
        return inside(1, 0)
    #elif number == 2:
    #    return inside(1, inside(array[2], 0))
   # elif number == 3:
      #  return inside(1, inside(array[2], inside(array[3], 0)))
    else:
        cont = number - 2
        ind = 1
        while cont >= 0:
            if cont > 0:
                cont -= 1

            place = inside(array[ind + 1], cont)
            output = inside(1, place)
            ind += 1
            return output



# Fraction(1, array[1] + Fraction(1, array[2] + Fraction(1, array[3])))

expansion = [2, 1]
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
print(expansion[0] + fractionalSum(4, expansion))
