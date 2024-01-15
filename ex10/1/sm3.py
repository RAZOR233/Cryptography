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
    # print(hex(int(binText, 2))[2:])
    # print(len(hex(int(binText, 2))[2:]))
    return binText
def pad1(ming):
    binText = ming
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
    # print(hex(int(binText, 2))[2:])
    # print(len(hex(int(binText, 2))[2:]))
    return binText

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
def left_move(t,n):
    list='{:032b}'.format(t)
    tmp=list[n:len(list)] + list[0:n]
    return int(tmp,2)

def extend(B):
    W=[0 for i in range(68)]
    W1 = [0 for i in range(64)]
    for i in range(16):
        W[15-i]=(B>>32*i)&(2**32-1)
    for j in range(16,68):
        W[j]=P(W[j-16]^W[j-9]^left_move(W[j-3],15),1)^left_move(W[j-13],7)^W[j-6]
    for j in range(64):
        W1[j]=W[j]^W[j+4]
    # for i in W1:
    #     print(hex(i))
    return W,W1
def CF(W,W1,h0):
    A = h0[0]
    B = h0[1]
    C = h0[2]
    D = h0[3]
    E = h0[4]
    F = h0[5]
    G = h0[6]
    H = h0[7]
    h = [A, B, C, D, E, F, G, H]
    for j in range(64):
        '''print(hex(A))
        print(hex(B))
        print(hex(C))
        print(hex(D))
        print(hex(E))
        print(hex(F))
        print(hex(G))
        print(hex(H))'''
        temp1 = left_move(A, 12)
        temp2 = left_move(T(j), j % 32)
        temp4 = (temp1 + E + temp2) & 0xFFFFFFFF
        SS1 = left_move(temp4, 7)
        SS2 = SS1 ^ temp1
        TT1 = (FF(A, B, C, j) + D + SS2 + W1[j]) & 0xFFFFFFFF
        TT2 = (GG(E, F, G, j) + H + SS1 + W[j]) & 0xFFFFFFFF
        D = C
        C = left_move(B, 9)
        B = A
        A = TT1
        H = G
        G = left_move(F, 19)
        F = E
        E = P(TT2,0)
    h[0] = h[0] ^ A
    h[1] = h[1] ^ B
    h[2] = h[2] ^ C
    h[3] = h[3] ^ D
    h[4] = h[4] ^ E
    h[5] = h[5] ^ F
    h[6] = h[6] ^ G
    h[7] = h[7] ^ H
    return h
def FF(X, Y, Z, j):
    if 0 <= j <= 15:
        return X ^ Y ^ Z
    elif 16 <= j <= 63:
        return (X & Y) | (X & Z) | (Y & Z)
def T(j):
    if 0 <= j <= 15:
        return 0x79cc4519
    elif 16 <= j <= 63:
        return 0x7a879d8a
def GG(X, Y, Z, j):
    if 0 <= j <= 15:
        return X ^ Y ^ Z
    elif 16 <= j <= 63:
        return (X & Y) | ((~X) & Z)


def P(X,op):
    if op==0:
        return X^left_move(X,9)^left_move(X,17)
    else:
        return X^left_move(X,15)^left_move(X,23)
def hash(m):
    h0 = [0x7380166f, 0x4914b2b9, 0x172442d7, 0xda8a0600, 0xa96f30bc, 0x163138aa, 0xe38dee4d, 0xb0fb0e4e]
    EM = pad(m)
    fenzu = len(EM) // 512
    M = []
    h = h0
    for i in range(fenzu):
        M.append(int(EM[512 * i:512 * (i + 1)], 2))
    for k in M:
        W, W1 = extend(k)
        h = CF(W, W1, h)
    result = 0
    for k in range(len(h)):
        result = result << 32 | h[k]
    return '{:064x}'.format(result)
def hash1(m):
    h0 = [0x7380166f, 0x4914b2b9, 0x172442d7, 0xda8a0600, 0xa96f30bc, 0x163138aa, 0xe38dee4d, 0xb0fb0e4e]
    EM = pad1(m)
    fenzu = len(EM) // 512
    M = []
    h = h0
    for i in range(fenzu):
        M.append(int(EM[512 * i:512 * (i + 1)], 2))
    for k in M:
        W, W1 = extend(k)
        h = CF(W, W1, h)
    result = 0
    for k in range(len(h)):
        result = result << 32 | h[k]
    return '{:064x}'.format(result)
if __name__ == "__main__":
  m = input()
  print(hash(m))
