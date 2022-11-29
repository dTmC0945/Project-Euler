
def number2text(n):
    number_dict = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9,
                   "eleven": 11, "twelve": 12, "thirteen": 13, "twenty": 20, "thirty": 30, "fourty": 40, "fifty": 50,
                   "sixty": 60, "seventy": 70, "eighty": 80, "ninety": 90, "one hundred": 100}
    number_value = list(number_dict.values())
    number_text = list(number_dict.keys())

    for index in range(0,len(number_value)):
        if number_value[index] == n:
            output = number_text[index]

    return output


print(number2text(21))