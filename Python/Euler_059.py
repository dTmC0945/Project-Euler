def xor(value_text, key_text):
    def Encryption(bit_Value, bit_Key):
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

all_freq = {}

for i in binary_array:
    if i in all_freq:
        all_freq[i] += 1
    else:
        all_freq[i] = 1

print(dict(sorted(all_freq.items(), key=lambda item: item[1])))

binary_array = ''.join(binary_array)


def binaryMaker(key_text, value_text):
    encryption_Key_Text = key_text

    binary = ','.join(format(ord(x), 'b') for x in encryption_Key_Text).split(",")

    ind = 0
    for value in binary:
        while len(binary[ind]) < 8:
            binary[ind] = "0" + binary[ind]
        ind += 1

    binary = "".join(binary)

    encrypted_List = value_text

    ind = 0
    binary_array = ','.join(format(ord(x), 'b') for x in encrypted_List).split(",")
    for e in encrypted_List:
        #binary_array.append(str(bin(e)[2:]))
        while len(binary_array[ind]) < 8:
            binary_array[ind] = "0" + binary_array[ind]
        ind += 1

    binary_array = "".join(binary_array)

    return binary, binary_array


binaryMaker("42", "65")
# repeat = int(len(binary_array) / len(binary))

# keyys = binary * repeat

# print(decoding(Encryption(binary_array, keyys)))
