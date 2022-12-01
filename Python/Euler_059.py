# implement the exclusive or encryption
def xorEncryption(bit_Value, bit_Key):  # takes in the bit values of the text and the key (all as one string)

    # does the magic encryption checks if the bits in each string matches or differs
    encryption = map(lambda v: 1 if bit_Value[v] != bit_Key[v] else 0, range(0, len(bit_Key)))

    # joins the output of the encryption
    join_Digits = "".join(map(str, list(encryption)))

    # returns the encrypted bits as one string
    return join_Digits


# executes the decoding of the ASCII values to characters
def decoding(binary_value):

    # separates the bits into 8 bit chunks to convert it to ASCII value
    segmented_Bits = [binary_value[bit:bit + 8] for bit in range(0, len(binary_value), 8)]

    # takes the 8 bit chunks and spews out the ASCII value
    character = list(map(lambda x: chr(int(x, 2)), segmented_Bits))

    # returns the ASCII value
    return character


# open the textfile
with open('Euler_059.txt') as file:
    lines = file.readlines()

encrypted_List = list(map(int, lines[0].split(",")))
encrypted_Char = [chr(encrypted_List[n]) for n in range(0,len(encrypted_List))]
#print(encrypted_Char)
binary_array = []

all_freq = {}

for i in encrypted_Char:
    if i in all_freq:
        all_freq[i] += 1
    else:
        all_freq[i] = 1


#print(dict(sorted(all_freq.items(), key=lambda item: item[1])))

binary_array = ''.join(binary_array)


def binaryMaker(key_text, value_text):
    encryption_Key_Text = key_text

    binary = ','.join(format(ord(x), 'b') for x in encryption_Key_Text).split(",")

    for ind in range(0, len(binary)):
        while len(binary[ind]) < 8:
            binary[ind] = "0" + binary[ind]
        ind += 1

    binary = "".join(binary)

    encrypted_List = value_text

    ind = 0
    binary_array = ','.join(format(ord(x), 'b') for x in encrypted_List).split(",")
    for e in encrypted_List:
        # binary_array.append(str(bin(e)[2:]))
        while len(binary_array[ind]) < 8:
            binary_array[ind] = "0" + binary_array[ind]
        ind += 1

    binary_array = "".join(binary_array)

    return binary, binary_array


text, key = binaryMaker("k", "*")

encrypt = xorEncryption(text, key)

print(decoding(encrypt))
# repeat = int(len(binary_array) / len(binary))

# keyys = binary * repeat

# print(decoding(Encryption(binary_array, keyys)))
