# checks if a number is palindrome by converting it into a string, reversing it and checking if it still matches.
def palindromeChecker(a, b):
    n = a * b

    text = str(n)

    reverse = text[::-1]

    if text == reverse:
        return n


bigValue = 0 # value assigned to keep only the biggest values

for a in range(1, 1000):
    for b in range(1, 1000):
        if len(str(a)) == 3 & len(str(b)) == 3:
            number = palindromeChecker(a, b)
            if number is None: # a error catcher for when the palindromeChecker returns a None
                number = 0
            if number > bigValue:
                bigValue = number

print(bigValue)
