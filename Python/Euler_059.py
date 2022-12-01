
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
print(encrypted_List)
encryption_Key_Text = "the"

binary = ''.join(format(ord(x), 'b') for x in encryption_Key_Text)

print(binary)