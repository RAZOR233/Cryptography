'''
Hill密码已知明文攻击
'''
# 搞错了，右乘是按行加密
import array


def ord_to_num(a):  # 将字符变成字母编码0-25
    return ord(a) - ord('a')

def num_to_ord(n):  # 将字符变成字母编码0-25
    return chr(ord('a') + n)


# def hill_doWork(A, t):  # 矩阵A乘字符串t mod26意义下。
#     # 传入A为n阶方阵，t为长度为n的字符串
#     # 返回值为加密后的字符串
#     # 调用函数ord_to_num, num_to_ord
#     n = len(t)  # 求长度
#     mess = []
#     for i in t:  # 字符串转数字编码列表
#         mess.append(ord_to_num(i))  # 逐个字符处理成列表
#
#     result = ""  # 空字符串用来存放这一组字符串加密后的结果
#     for i in range(n):  # 矩阵乘法
#         temp = 0
#         for j in range(n):
#             temp += A[j][i] * mess[j]  # 字符串右乘矩阵
#         result += num_to_ord(temp % 26)  # 转换为mod 26字符
#     return result


def submatrix(A, i, j):  # 求矩阵的余子矩阵，返回余子矩阵-用于求逆矩阵
    # 矩阵A第i行第j列元素的余矩阵
    p = len(A)  # 矩阵的行数
    q = len(A[0])  # 矩阵的列数
    C = [[A[x][y] for y in range(q) if y != j] for x in range(p) if x != i]  # 列表推导式
    return C


def det(A):  # 求矩阵行列式，返回mod26数值-用于求逆矩阵
    # 按第一行展开递归求矩阵的行列式
    # 调用到函数det, submartrix
    p = len(A)  # 矩阵的行数
    q = len(A[0])  # 矩阵的列数
    if (p == 1 and q == 1):
        return A[0][0] %26
    else:
        value = 0
        for j in range(q):
            value += ((-1) ** (j + 2)) * A[0][j] * det(submatrix(A, 0, j))
            value = value % 26  # 这里添加了mod
        return value


def inverseNum(a, b=26):  # 输入a,p，给出a 的逆元-用于求逆矩阵
    a1, a2 = 1, 0
    b1, b2 = 0, 1
    r = 1  # 设置初始值，以保证下面的循环可以启动
    while r != 0:  # 行列式变换
        q = a // b
        r = a % b
        c = a - b * q
        c1 = a1 - b1 * q
        c2 = a2 - b2 * q
        a, a1, a2 = b, b1, b2
        b, b1, b2 = c, c1, c2
    if a < 0:  # 避免gcd的结果是负数
        a, a1, a2 = -a, -a1, -a2
    return a1  # 这里返回的是g，系数x,y ， xa + yb = g


def arrayInverse(A):  # 求矩阵的逆矩阵，返回逆矩阵
    '''注意一个问题，偶数没有逆元 所以要判断det'''
    # 矩阵mod26求逆，需要用到函数det, inverseNum, submatrix
    p = len(A)  # 矩阵的行数
    q = len(A[0])  # 矩阵的列数
    C = [[0 for i in range(q)] for i in range(p)]  # 这里进行了修改
    d = det(A)
    for i in range(p):
        for j in range(q):
            C[i][j] = (((-1) ** (i + j + 2)) * det(submatrix(A, j, i))) % 26
            C[i][j] = (C[i][j] * inverseNum(d, 26)) % 26
    return C


# def hill_encode(k, mess, n):  # Hill密码加密算法
#     # 调用函数 hill_doWork
#     cipher = ""
#     num = len(mess) // n  # 求出一共有多少组 使用整除将结果化为整形，因为题目中保证整除性
#     for i in range(num):
#         temp = mess[i * n: i * n + n]
#         c = hill_doWork(k, temp)  # 调用矩阵字符串加密算法
#         cipher += c
#     return cipher

def getArray(mess, n):
    array = []  #
    for i in range(n):  # 按行提取密文，构成矩阵
        lis = []
        for j in range(n):
            lis.append(ord_to_num(mess[i*n+j])) #
        array.append(lis)
    # print(array)
    return array

def arrayMulti(A, B):   # 同阶方阵乘法
    n = len(A)  # 获得阶数
    C = []
    for i in range(n):
        lis = []    # 逐行处理
        for j in range(n):  # 处理C[i][j]
            temp = 0
            for t in range(n):
                temp += (A[i][t] * B[t][j]) % 26    # A的i行*B的j列
            lis.append(temp%26)
        C.append(lis)
    return C


def hill_attack(mess,cipher, n):
    messLis = getArray(mess, n)     # M
    cipherLis = getArray(cipher, n) # C
    d = det(messLis)
    i = 1
    while d % 2 == 0 or d%13 == 0:  # 如果messLis不能求逆，那么就往后n个字符
        messLis = getArray(mess[i*n:] , n)
        i += 1
        d = det(messLis)
    print(i)
    if i != 1:  # 将cipher和mess对齐
        cipherLis = getArray(cipher[i * n-n:], n)
    messInver = arrayInverse(messLis)   # 求M‘
    Key = arrayMulti(messInver, cipherLis)  # K = M'C
    return Key


n = int(input(""))
Mess = input("").strip('\r')
Cipher = input("").strip('\r')
key = hill_attack(Mess,Cipher,n)
for i in range(len(key)):
    for j in range(len(key)):
        print("{} ".format(key[i][j]), end="")
    print("")