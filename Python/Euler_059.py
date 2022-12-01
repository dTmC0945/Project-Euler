
def xorEncryption(value, key):
    bit_Value, bit_Key = bin(value)[2:], bin(key)[2:]
    print(bit_Value)
    print(bit_Key)
    return list(map(lambda v: 1 if bit_Value[v] != bit_Key[v] else 0, range(0, len(bit_Key))))


print(xorEncryption(65, 42))