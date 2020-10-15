with open("flag", "r") as f:
    flag = f.read()

table_plain = [196, 68, 122, 155, 80, 73, 11, 84, 221, 231, 197, 17, 254, 54, 251, 227, 24, 159, 179, 30, 241, 25, 99, 56, 166, 142, 195, 178, 78, 149, 218, 225, 214, 200, 87, 198, 27, 236, 230, 191, 32, 102, 79, 141, 107, 245, 193, 202, 90, 100, 163, 131, 213, 212, 8, 133, 15, 183, 243, 96, 158, 40, 220, 106, 235, 188, 18, 2, 249, 132, 69, 253, 72, 28, 1, 177, 34, 194, 207, 33, 110, 26, 246, 6, 228, 57, 140, 173, 115, 167, 108, 111, 127, 13, 217, 156, 192, 59, 143, 38, 48, 62, 180, 50, 35, 138, 23, 128, 14, 124, 91, 95, 152, 119, 162, 240, 70, 5, 20, 165, 21, 66, 121, 151, 76, 125, 175, 146, 46, 4, 89, 145, 204, 82, 51, 41, 129, 58, 168, 120, 185, 10, 182, 154, 203, 118, 216, 222, 208, 47, 29, 219, 53, 255, 112, 199, 81, 93, 71, 113, 97, 137, 39, 232, 134, 98, 229, 83, 130, 223, 186, 42, 114, 44, 85, 242, 176, 92, 189, 67, 148, 77, 209, 187, 147, 60, 45, 161, 63, 105, 233, 16, 52, 55, 160, 9, 250, 116, 0, 94, 37, 234, 247, 210, 224, 238, 126, 237, 244, 61, 101, 136, 31, 171, 201, 248, 164, 135, 109, 65, 170, 150, 172, 88, 144, 205, 12, 103, 104, 215, 211, 252, 19, 86, 184, 190, 226, 49, 36, 74, 3, 174, 22, 157, 123, 181, 206, 153, 64, 239, 7, 43, 117, 75, 139, 169]
table_nibble = [6, 1, 10, 12, 9, 7, 5, 14, 15, 13, 11, 3, 0, 4, 2, 8]
table_cipher = [105, 179, 59, 248, 159, 35, 145, 14, 43, 20, 140, 212, 227, 251, 185, 71, 153, 243, 39, 236, 188, 17, 90, 148, 142, 230, 4, 254, 55, 187, 107, 121, 25, 6, 119, 94, 224, 110, 16, 150, 83, 88, 166, 9, 103, 245, 81, 50, 106, 131, 216, 63, 12, 91, 157, 137, 165, 175, 98, 0, 3, 253, 156, 5, 136, 42, 64, 247, 222, 82, 238, 41, 237, 246, 226, 203, 208, 199, 126, 1, 48, 29, 66, 24, 255, 27, 127, 195, 87, 79, 109, 97, 118, 144, 173, 65, 75, 95, 213, 198, 114, 61, 26, 146, 67, 32, 168, 92, 11, 193, 190, 178, 46, 102, 189, 15, 80, 242, 51, 96, 180, 218, 134, 117, 129, 155, 21, 56, 206, 47, 130, 45, 138, 73, 184, 104, 112, 85, 221, 124, 2, 202, 7, 147, 125, 60, 69, 231, 229, 201, 172, 139, 215, 40, 49, 76, 170, 196, 70, 10, 23, 235, 223, 111, 149, 241, 77, 135, 152, 34, 220, 192, 181, 86, 133, 132, 249, 52, 211, 233, 18, 210, 120, 183, 154, 72, 74, 33, 194, 100, 163, 123, 108, 115, 53, 209, 58, 28, 99, 158, 31, 228, 161, 197, 143, 141, 234, 44, 219, 62, 78, 244, 250, 225, 30, 57, 176, 128, 122, 116, 101, 162, 68, 54, 217, 160, 186, 169, 93, 19, 191, 36, 89, 240, 8, 38, 232, 177, 37, 151, 174, 13, 113, 252, 84, 204, 182, 200, 239, 22, 164, 214, 207, 171, 205, 167]

flag = [int(flag[i:i+2], 16) for i in range(0, len(flag), 2)]

def sub_from_table_plain(x):
    global table_plain
    res = table_plain[x]
    table_plain = table_plain[1:] + table_plain[:1]
    return res

def reverse_sub_from_table_plain(x):
    global table_plain
    res = table_plain.index(x)
    table_plain = table_plain[1:] + table_plain[:1]
    return res

def sub_from_table_nibble(x):
    global table_nibble
    x1 = table_nibble[x & 0xf]
    x2 = table_nibble[x >> 4]
    return (x1 << 4) + x2

def reverse_sub_from_table_nibble(x):
    global table_nibble
    x1 = table_nibble.index(x & 0xf)
    x2 = table_nibble.index(x >> 4)
    return (x1 << 4) + x2

def rol(x):
    b = "{:08b}".format(x)
    b = b[2:] + b[:2]
    return int(b, 2)

def ror(x):
    b = "{:08b}".format(x)
    b = b[-2:] + b[:-2]
    return int(b, 2)

def xor_table_cipher(iv):
    global table_cipher
    for i in range(256):
        table_cipher[i] ^= iv[2]

def xor_table_cipher2(iv):
    global table_plain, table_cipher
    for i in range(256):
        table_cipher[i] = (table_cipher[i] + iv[0]) % 256
        table_plain[i] ^= iv[4]


# recover random iv
# known plaintext => gemna
pl = [ord(i) for i in list('gemas')]
pl = [sub_from_table_plain(i) for i in pl]
pl = [sub_from_table_nibble(i) for i in pl]
pl = [rol(i) for i in pl]

iv = []
for i in range(5):
    pl[i] ^= (pl[i] & 0xf) << 4
    inx = table_cipher.index(flag[i]) ^ pl[i]
    iv.append(inx)
    iv[i] = (iv[i] + flag[i]) % 256

xor_table_cipher(iv)
xor_table_cipher2(iv)

plaintext = 'gemas'

# recover flag
for i in range(5, len(flag), 5):
    ct = [flag[i] for i in range(i, i+5)]

    for i in range(5):
        pl = table_cipher.index(ct[i]) ^ iv[i]
        pl ^= (pl & 0xf) << 4
        pl = ror(pl)
        pl = reverse_sub_from_table_nibble(pl)
        pl = reverse_sub_from_table_plain(pl)
        plaintext += chr(pl)
        iv[i] = (iv[i] + ct[i]) % 256
    xor_table_cipher(iv)
    xor_table_cipher2(iv)

print(plaintext)

