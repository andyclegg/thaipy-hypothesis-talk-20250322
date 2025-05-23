import string

base64_characters = string.ascii_uppercase + string.ascii_lowercase + string.digits + '+/'
assert len(base64_characters) == 64

def my_b64_encode(x):
    binary_8bit = ''.join(format(byte, '08b') for byte in x)
    binary_6bit_chunks = ['00' + binary_8bit[x:x+6] for x in range(0, len(binary_8bit), 6)]
    return  ''.join(base64_characters[int(x,2)] for x in binary_6bit_chunks).encode('ascii')


def my_b64_decode(x):
    data_points = [base64_characters.index(c) for c in x.decode('ascii')]
    binary_6bit = ''.join(format(a, '06b') for a in data_points)
    binary_8bit_chunks = [binary_6bit[x:x+8] for x in range(0, len(binary_6bit), 8)]
    return bytes(int(x,2) for x in binary_8bit_chunks)



