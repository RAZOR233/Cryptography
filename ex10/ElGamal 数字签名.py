import gmpy2
import hashlib
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
q=int(input())
a=int(input())
M=input()
mode=input()
if mode=="Sign":
    x=int(input())
    k=int(input())
    t=str_2_bin(M)
    byte_num = len(t) // 8
    if len(t) % 8 != 0:
        byte_num += 1
    m = int("0x" + hashlib.sha256(int.to_bytes(int(t, 2), byte_num, byteorder='big')).hexdigest(), 16)
    s1=gmpy2.powmod(a,k,q)
    s2=gmpy2.invert(k,q-1)*(m-x*s1) % (q-1)
    print(s1,s2)
else:
    y=int(input())
    s1,s2= map(int, input().split())
    t = str_2_bin(M)
    byte_num = len(t) // 8
    if len(t) % 8 != 0:
        byte_num += 1
    m = int("0x" + hashlib.sha256(int.to_bytes(int(t,2), byte_num, byteorder='big')).hexdigest(), 16)
    v1=gmpy2.powmod(a,m,q)
    v2=gmpy2.powmod(y,s1,q)*gmpy2.powmod(s1,s2,q)%q
    if v1==v2:
        print("True")
    else:
        print("False")