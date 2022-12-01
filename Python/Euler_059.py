import binascii


def xorEncryption(bit_Value, bit_Key):
    while len(bit_Value) != len(bit_Key):
        if len(bit_Value) > len(bit_Key):
            bit_Key = "0" + bit_Key
        else:
            bit_Value = "0" + bit_Value
    encryption = map(lambda v: 1 if bit_Value[v] != bit_Key[v] else 0, range(0, len(bit_Key)))
    join_Digits = "".join(map(str, list(encryption)))
    return join_Digits


def decoding(binary_value):
    line = [binary_value[i:i + 8] for i in range(0, len(binary_value), 8)]
    charlist = list(map(lambda x: chr(int(x, 2)), line))
    return charlist


# open the textfile
with open('Euler_059.txt') as file:
    lines = file.readlines()

encrypted_List = list(map(int, lines[0].split(",")))

binary_array = []
index = 0

for e in encrypted_List:
    binary_array.append(str(bin(e)[2:]))
    while len(binary_array[index]) < 8:
        binary_array[index] = "0" + binary_array[index]
    index += 1

encryption_Key_Text = "god"

binary_array = ''.join(binary_array)

binary = ','.join(format(ord(x), 'b') for x in encryption_Key_Text).split(",")

index = 0
for value in binary:
    while len(binary[index]) < 8:
        binary[index] = "0" + binary[index]
    index += 1

binary = "".join(binary)

repeat = int(len(binary_array) / len(binary))

keyys = binary * repeat

print(decoding(xorEncryption(binary_array, keyys)))
