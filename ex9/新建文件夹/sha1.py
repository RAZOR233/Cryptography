def pad(ming):
    binText = str_2_bin(ming)
    # print(len(binText)-2**64)
    initLen = binLen = len(binText)
    binText += '1'
    binLen += 1
    while binLen % 512 != 448:
        binText += '0'
        binLen += 1
    temp = bin(initLen)[2:]
    lentemp = len(temp)
    while lentemp != 64:
        temp = '0' + temp
        lentemp += 1
    binText = binText + temp
    # print(binText)
    return binText


def padhex(ming):
    binText = hex_2_bin(ming)
    initLen = binLen = len(binText)
    binText += '1'
    binLen += 1
    while binLen % 512 != 448:
        binText += '0'
        binLen += 1
    temp = bin(initLen)[2:]
    lentemp = len(temp)
    while lentemp != 64:
        temp = '0' + temp
        lentemp += 1
    binText = binText + temp
    # print(binText)
    return binText


def hex_2_bin(strr):
    result = ''
    for i in strr:
        x = bin(int('0x'+i, 16))[2:]
        while len(x) < 4:
            x = '0' + x
        result += x
    return result


def str_2_bin(strr):
    result = ''
    for i in strr:
        x = bytes(i, encoding="utf-8")
        for j in x:
            y = bin(j)[2:]
            while len(y) % 8 != 0:
                y = '0' + y
            result += y
    return result


def Hash1(ming):
    h0 = [0x67452301, 0xefcdab89, 0x98badcfe, 0x10325476, 0xc3d2e1f0]
    EM = padhex(ming)
    # print(len(EM))
    fenzu = len(EM) // 512
    M = []
    h = h0
    for i in range(fenzu):
        M.append(EM[512 * i:512 * (i + 1)])
    for j in range(len(M)):
        W = extend(M[j])
        h = Round(W, h)
    result = 0
    for k in range(len(h)):
        result = result << 32 | h[k]
    # print(hex(result))
    return result


def Hash(ming):
    h0 = [0x67452301, 0xefcdab89, 0x98badcfe, 0x10325476, 0xc3d2e1f0]
    EM = pad(ming)
    # print(len(EM))
    fenzu = len(EM) // 512
    M = []
    h = h0
    for i in range(fenzu):
        M.append(EM[512 * i:512 * (i + 1)])
    for j in range(len(M)):
        W = extend(M[j])
        h = Round(W, h)
    result = 0
    for k in range(len(h)):
        result = result << 32 | h[k]
    print(len(hex(result)[2:]))
    return result


def extend(M):
    W = []
    for i in range(16):
        W.append(int(M[32 * i:32 * (i + 1)], 2))
    '''for i in range(16):
        print(bin(W[i]))'''
    for j in range(16, 80):
        temp = W[j - 3] ^ W[j - 8] ^ W[j - 14] ^ W[j - 16]
        temp = ((temp << 1) & 0b11111111111111111111111111111110) | temp >> 31
        # print(bin(temp))
        W.append(temp)
    return W


def Round(W, h0):
    a = h0[0]
    b = h0[1]
    c = h0[2]
    d = h0[3]
    e = h0[4]
    h = [a, b, c, d, e]
    for i in range(80):
        temp1 = ((a << 5) & 0b11111111111111111111111111100000) | a >> 27
        temp2 = f(b, c, d, i)
        temp3 = e
        temp4 = W[i]
        temp5 = K(i)
        temp = (temp1 + temp2 + temp3 + temp4 + temp5) % 2 ** 32
        e = d
        d = c
        c = ((b << 30) & 0b11000000000000000000000000000000) | b >> 2
        b = a
        a = temp
    '''print(bin(a))
    print(bin(b))
    print(bin(c))
    print(bin(d))
    print(bin(e))'''
    h[0] = (h[0] + a) % 2 ** 32
    h[1] = (h[1] + b) % 2 ** 32
    h[2] = (h[2] + c) % 2 ** 32
    h[3] = (h[3] + d) % 2 ** 32
    h[4] = (h[4] + e) % 2 ** 32
    '''for i in range(5):
        print(hex(h[i]))'''
    return h


def f(b, c, d, i):
    result = 0
    if 0 <= i < 20:
        result = (b & c) | ((~b) & d)
    elif 20 <= i < 40:
        result = b ^ c ^ d
    elif 40 <= i < 60:
        result = (b & c) | (b & d) | (c & d)
    elif 60 <= i < 80:
        result = b ^ c ^ d
    return result


def K(i):
    result = 0
    if 0 <= i < 20:
        result = 0x5a827999
    elif 20 <= i < 40:
        result = 0x6ed9eba1
    elif 40 <= i < 60:
        result = 0x8f1bbcdc
    elif 60 <= i < 80:
        result = 0xca62c1d6
    return result

if __name__ == "__main__":
    m=input()
    print(hex(Hash(m))[2:])

