
import gmpy2
import hashlib
import math
def multiply(Q,n, a,b,p):
    result = [0, 0]
    while n > 0:
        if n & 1:
            result = add(result, Q,a,b,p)
        n >>= 1
        Q = add(Q, Q,a,b,p)
    return result


def add(P, Q,a,b,p):
    if P == [0, 0]:
        return Q
    result = [0, 0]
    if P == Q:
        lamb = ((3 * P[0] * P[0] % p + a) * gmpy2.invert(2 * P[1], p)) % p
    else:
        lamb = (Q[1] - P[1]) % p * gmpy2.invert(Q[0] - P[0], p) % p
    result[0] = (lamb * lamb - P[0] - Q[0]) % p
    result[1] = (lamb * (P[0] - result[0]) - P[1]) % p
    return result
def kdf(Z,klen):
    ct=0x00000001
    rg=math.ceil(klen/256)
    # print(rg)
    Ha=[]
    for i in range(rg):
        CT=str(hex(ct)[2:]).zfill(8)
        Ha.append(hashlib.sha256(bytes.fromhex(Z+CT)).hexdigest())
        # print(Ha)
        ct+=1
    # print(Ha)
    if klen%256!=0:
        # Ha[rg-1]=int(Ha[rg-1],16)>>(len(bin(int(Ha[rg-1],16))[2:])-klen+Par*(klen//Par))
        # print(len(bin(int(Ha[rg-1],16))[2:])-klen+Par*(klen//Par),Par - klen + Par * (klen // Par))
        Ha[rg - 1] =hex( int(Ha[rg - 1], 16) >> (256 - klen + 256 * (klen // 256)))[2:]
    # print(hex(Ha[0]))
    K=''
    for i in range(rg):K+=Ha[i]
    # print(len(K))
    return K
def fill(input,n):
    t=hex(input)[2:]
    while len(t)<n:
        t="0"+t
    return t
def fill_to_specific_bits(s,bits):
    while len(s) != bits:
        s = "0" + s
    return s
def point_to_bits(P,mode,par):
    x = bin(P[0]).replace('0b','')
    y = bin(P[1]).replace('0b','')
    x = fill_to_specific_bits(x,par)
    y = fill_to_specific_bits(y,par)
    if mode == 0:
        return x , y
    else: return "00000100" + x + y
p=int(input())
a=int(input())
b=int(input())
x,y= map(str, input().split())
G=[int(x),int(y)]
Par=int(input())
op=int(input())
m=int(input(),16)
if op==1:
    x, y = map(str, input().split())
    PB = [int(x), int(y)]
    k=int(input())
    C1 = multiply(G, k, a, b, p)
    # print(C1)
    x2, y2 = multiply(PB, k, a, b, p)
    klen = len(bin(m)[2:])
    while klen % 4 != 0:
        klen += 1
    # print("klen",klen)
    X2 = fill(x2, Par // 4)
    Y2 = fill(y2, Par // 4)
    t = kdf(X2 + Y2, klen)
    # print(t)
    C2 = m ^ int(t, 16)
    # print(C2)
    # print(len(y2))
    tmp = (x2 << (Par + klen)) + (m << Par) + y2
    # print(hex(C1[0])[2:],hex(C1[1])[2:])
    # print(hex(tmp))
    byte_num = len(bin(tmp)[2:]) // 8
    if len(bin(tmp)[2:]) % 8 != 0:
        byte_num += 1
    c3_tmp = int("0b" + bin(tmp)[2:], 2)
    C3 = hashlib.sha256(int.to_bytes(c3_tmp, byte_num, byteorder='big')).hexdigest()
    C1_string = point_to_bits(C1, 1, Par)
    C2_string = fill_to_specific_bits(bin(C2).replace('0b', ''), klen)
    C3_string = fill_to_specific_bits(bin(int("0x" + C3, 16)).replace('0b', ''), 256)
    # C3 = hashlib.sha256(bytes.fromhex(hex(tmp)[2:].zfill((2*Par+klen)//4))).hexdigest()
    # print(hex(C2))
    # print(hex(x1),hex(y1),C3,hex(C2))
    print(hex(int("0b"+ C1_string + C2_string + C3_string,2)).replace('0x','0x0'))
else:
    dB = int(input())
    C=hex(m)[3:]
    x=int(C[0:Par//4],16)
    y=int(C[Par//4:2*Par//4],16)
    C1=[x,y]
    C2=int(C[2*Par//4:len(C)-256//4],16)
    C3=int(C[len(C)-256//4:],16)
    # print(hex(C2))
    # print(hex(C3))
    x2,y2=multiply(C1,dB,a,b,p)
    klen = len(bin(C2)[2:])
    while klen % 4 != 0:
        klen += 1
    # print(klen)
    X2 = fill(x2, Par // 4)
    Y2 = fill(y2, Par // 4)
    t = kdf(X2 + Y2, klen)
    M=C2^int(t,16)
    print(hex(M))
    # tmp = (x2 << (Par + klen)) + (m << Par) + y2
    # out = hashlib.sha256(bytes.fromhex(str(hex(tmp)[2:]))).hexdigest()
    # print(x,'\n',y)
#0x0423fc680b124294dfdf34dbe76e0c38d883de4d41fa0d4cf570cf14f20daf0c4d777f738d16b16824d31eefb9de31ee1fc83b3aca55b86298651e64547d69139b39d58f03a0017c01434a4d803ca01fd5736821047292b1615bc0f71e0e6270edcee7b3
#0x0423fc680b124294dfdf34dbe76e0c38d883de4d41fa0d4cf570cf14f20daf0c4d777f738d16b16824d31eefb9de31ee1fc83b3aca55b86298651e64547d69139b39d58f03a0017c01434a4d803ca01fd5736821047292b1615bc0f71e0e6270edcee7b3