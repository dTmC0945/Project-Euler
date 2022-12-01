def xorEncryption(bit_Value, bit_Key):
    while len(bit_Value) != len(bit_Key):
        if len(bit_Value) > len(bit_Key):
            bit_Key = "0" + bit_Key
        else:
            bit_Value = "0" + bit_Value
    encryption = map(lambda v: 1 if bit_Value[v] != bit_Key[v] else 0, range(0, len(bit_Key)))
    join_Digits = "".join(map(str, list(encryption)))
    return join_Digits, int(join_Digits, 2)


# bit_Value, bit_Key = bin(value)[2:], bin(key)[2:]
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

print(binary_array)

encryption_Key_Text = "the"

binary_array = ''.join(binary_array)

binary = ''.join(format(ord(x), 'b') for x in encryption_Key_Text)

repeat = print((len(binary_array)/len(binary)))


#print(xorEncryption(binary_array[5], binary))