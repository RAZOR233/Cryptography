import sys
IP=[58, 50, 42, 34, 26, 18, 10,  2, 60, 52, 44, 36, 28, 20, 12,  4,
62, 54, 46, 38, 30, 22, 14,  6, 64, 56, 48, 40, 32, 24, 16,  8,
57, 49, 41, 33, 25, 17,  9,  1, 59, 51, 43, 35, 27, 19, 11,  3,
61, 53, 45, 37, 29, 21, 13,  5, 63, 55, 47, 39, 31, 23, 15,  7]
IPI=[40,  8, 48, 16, 56, 24, 64, 32, 39,  7, 47, 15, 55, 23, 63, 31,
38,  6, 46, 14, 54, 22, 62, 30, 37,  5, 45, 13, 53, 21, 61, 29,
36,  4, 44, 12, 52, 20, 60, 28, 35,  3, 43, 11, 51, 19, 59, 27,
34,  2, 42, 10, 50, 18, 58, 26, 33,  1, 41,  9, 49, 17, 57, 25]
KS1=[57, 49, 41, 33, 25, 17,  9,  1, 58, 50, 42, 34, 26, 18,
10,  2, 59, 51, 43, 35, 27, 19, 11,  3, 60, 52, 44, 36,
63, 55, 47, 39, 31, 23, 15,  7, 62, 54, 46, 38, 30, 22,
14,  6, 61, 53, 45, 37, 29, 21, 13,  5, 28, 20, 12,  4]
KS2=[14, 17, 11, 24,  1,  5,  3, 28, 15,  6, 21, 10,
23, 19, 12,  4, 26,  8, 16,  7, 27, 20, 13,  2,
41, 52, 31, 37, 47, 55, 30, 40, 51, 45, 33, 48,
44, 49, 39, 56, 34, 53, 46, 42, 50, 36, 29, 32]
KE=[32,  1,  2,  3,  4,  5,  4,  5,  6,  7,  8,  9,
 8,  9, 10, 11, 12, 13, 12, 13, 14, 15, 16, 17,
16, 17, 18, 19, 20, 21, 20, 21, 22, 23, 24, 25,
24, 25, 26, 27, 28, 29, 28, 29, 30, 31, 32,  1 ]
KL=[1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]#0没有意义
PBox=[16,  7, 20, 21, 29, 12, 28, 17,  1, 15, 23, 26,  5, 18, 31, 10,
 2,  8, 24, 14, 32, 27,  3,  9, 19, 13, 30,  6, 22, 11,  4, 25]
SBox=[[]for i in range(0,9)]
SBox[1]=[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7,
0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8,
4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0,
15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]
SBox[2]=[15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10,
3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5,
0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15,
13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]
SBox[3]=[10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8,
13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1,
13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7,
1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]
SBox[4]=[7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15,
13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9,
10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4,
3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]
SBox[5]=[2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9,
14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6,
4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14,
11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]
SBox[6]=[12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11,
10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8,
9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6,
4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]
SBox[7]=[4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1,
13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6,
1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2,
6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]
SBox[8]=[13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7,
1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2,
7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8,
2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]
def list_to_str(list):
    str=""
    for i in list:
        str=i+str
    return str
def enIP(list):
    output=[0 for i in range(0,64)]
    for i in range(0,64):
        output[IP.index(i+1)]=list[63-i]
    tmp = list_to_str(output)
    return tmp
def enIPI(L,R):
    t1 = str(bin(L))[2:]
    while len(t1) != 32:
        t1 = '0' + t1
    t2 = str(bin(R))[2:]
    while len(t2) != 32:
        t2 = '0' + t2
    list = t2 + t1
    output=[0 for i in range(0,64)]
    for i in range(0,64):
        output[IPI.index(i+1)]=list[63-i]
    tmp = list_to_str(output)
    t=int(tmp,2)
    return t
def  Key_Substitution_1(list):
    output = [0 for i in range(0, 56)]
    for i in range(0, 56):
        output[55-i]= list[KS1[i]-1]####
    tmp = list_to_str(output)
    return tmp
def  P_Substitution(list):
    t = str(bin(list))[2:]
    while len(t) != 32:
        t = '0' + t
    output = [0 for i in range(0, 32)]
    for i in range(0, 32):
        output[31-i]= t[PBox[i]-1]####
    tmp = list_to_str(output)
    return tmp
def  Key_Substitution_2(C,D):
    list=C+D
    output = [0 for i in range(0, 48)]
    for i in range(0, 48):
        output[47-i]= list[KS2[i]-1]
    tmp = list_to_str(output)
    return tmp
def left_move(list,n):
    return list[n:len(list)]+list[0:n]
def Key_Extension(list):
    t = str(bin(list))[2:]
    while len(t) != 32:
        t = '0' + t
    output = ["0" for i in range(0, 48)]
    tmp=[]
    for i in range(0, 48):
        output[i] = t[32 - KE[i]]
    tmp = list_to_str(output)
    tmp="0b"+tmp
    return tmp
def Sbox(t2):
    S = [[0 for i in range(0, 6)] for j in range(0, 8)]
    Sout = [0 for i in range(0, 8)]
    B = [0 for i in range(0, 6)]
    out = 0
    L = 0b111111
    for i in range(0, 8):
        S[7 - i] = t2 & L
        t2 = t2 >> 6
    for i in range(0, 8):
        B[0] = S[i] & 1
        S[i] = S[i] >> 1
        B[1] = S[i] & 0b1111
        S[i] = S[i] >> 4
        B[2] = S[i] & 1
        h = B[0] + B[2] * 2
        l = B[1]
        Sout[i] = SBox[i + 1][h * 16 + l]
        out += Sout[i] << (4 * (7 - i))
    return out

def Key_creat(k):
    K = [[0 for i in range(0, 48)] for j in range(0, 17)]
    C = [[0 for i in range(0, 28)] for j in range(0, 17)]
    D = [[0 for i in range(0, 28)] for j in range(0, 17)]
    t = str(bin(k))[2:]
    while len(t) != 64:
        t = '0' + t
    t = Key_Substitution_1(t)
    C[0] = t[0:28]
    D[0] = t[28:56]
    for i in range(1, 17):
        C[i] = left_move(C[i - 1], KL[(i - 1) % 16])
        D[i] = left_move(D[i - 1], KL[(i - 1) % 16])
        K[i] = Key_Substitution_2(C[i], D[i])
    return K

def encode(s,k):
    L = [0 for j in range(0, 17)]
    R = [0 for j in range(0, 17)]
    t = str(bin(s))[2:]
    while len(t) != 64:
        t = '0' + t
    t = enIP(t)
    L[0] = int(t[0:32], 2)
    R[0] = int(t[32:64], 2)
    K = Key_creat(k)
    for i in range(0,16):
        Rt = Key_Extension(R[i])
        # Generate Key
        t2 = int(K[i+1], 2) ^ int(Rt, 2)
        # Sbox
        out = Sbox(t2)
        # Pbox
        t = int(P_Substitution(out), 2)
        # 赋值
        R[i+1] = t ^ L[i]
        L[i+1] = R[i]
    return enIPI(L[16], R[16])
def decode(s,k):
    L = [0 for j in range(0, 17)]
    R = [0 for j in range(0, 17)]
    t = str(bin(s))[2:]
    while len(t) != 64:
        t = '0' + t
    t = enIP(t)
    L[0] = int(t[0:32], 2)
    R[0] = int(t[32:64], 2)
    K = Key_creat(k)
    for i in range(0,16):
        Rt = Key_Extension(R[i])
        # Generate Key
        t2 = int(K[16-i], 2) ^ int(Rt, 2)
        # Sbox
        out = Sbox(t2)
        # Pbox
        t = int(P_Substitution(out), 2)
        # 赋值
        R[i+1] = t ^ L[i]
        L[i+1] = R[i]
    return enIPI(L[16], R[16])
def EDE(k1,k2,s):
    return encode(decode(encode(s, k1),k2),k1)
'''
39
0x02468aceeca86420
0x0f1571c947d9e859
0
'''
v=int(input(),16)

k1=int(input(),16)
k2=int(input(),16)
n=int(input())
# S=[[0 for i in range(0,64)] for j in range(0,n+1)]
# L=[[0 for i in range(0,32)] for j in range(0,n+1)]
# R=[[0 for i in range(0,32)] for j in range(0,n+1)]
# C=[[0 for i in range(0,28)] for j in range(0,n+1)]
# D=[[0 for i in range(0,28)] for j in range(0,n+1)]

for i in range(n):
    dt = int(input(), 16)
    t=EDE(k1,k2,dt)
    r=EDE(k1,k2,v^t)
    print("0x", end='')
    print('{:016x}'.format(r))
    v=EDE(k1,k2,r^t)
