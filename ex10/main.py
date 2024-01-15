import sm3
import gmpy2
import math
def multiply(Q,n, a,b,p):
    result = [0, 0]
    while n > 0:
        if n & 1:
            result = add(result, Q,a,b,p)
        n >>= 1
        Q = add(Q, Q,a,b,p)
    return result

def fill_to_specific_bits(s,bits):
    while len(s) != bits:
        s = "0" + s
    return s

def point_to_bits(P,mode):
    par = math.ceil(math.log(p,2))
    x = bin(P[0]).replace('0b','')
    y = bin(P[1]).replace('0b','')
    x = fill_to_specific_bits(x,par)
    y = fill_to_specific_bits(y,par)
    if mode == 0:
        return x , y
    else: return "00000100" + x + y
def get_Z(id,P,G,a,b):
    id_ = id.encode('utf-8').hex()
    entl='{:016b}'.format(len(sm3.str_2_bin(id)))
    id_bin = bin(int(id_, 16))[2:].zfill(len(id_) * 4)
    a_bin = bin(a)[2:]
    while len(a_bin) % 8 != 0:
        a_bin = "0" + a_bin
    b_bin = bin(b)[2:]
    while len(b_bin) % 8 != 0:
        b_bin = "0" + b_bin
    xg,yg = point_to_bits(G,0)
    xp,yp = point_to_bits(P,0)
    bin_string = entl + id_bin + a_bin + b_bin + xg + yg + xp + yp
    Z = sm3.hash1(bin_string)
    return Z
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
def pad(a):
    t=a
    if len(t)%8!=0:
        t='0'+t
    return t
p=int(input())
a=int(input())
b=int(input())
x,y= map(str, input().split())
G=[int(x),int(y)]
n=int(input())
id=input()
x1,y1= map(str, input().split())
P=[int(x1),int(y1)]
M=input()
op=input()
if op=="Sign":
    d = int(input())
    k = int(input())
    Z=get_Z(id,P,G,a,b)
    t=Z+M.encode("utf-8").hex()
    tt=bin(int(t,16))[2:].zfill(len(t)*4)
    e=sm3.hash1(tt)
    T=multiply(G,k,a,b,p)
    r=(int(e,16)+T[0])%n
    s=gmpy2.invert(1+d,n)*(k-r*d)%n
    print(r)
    print(s)
else:
    r = int(input())
    s = int(input())
    Z = get_Z(id, P, G, a, b)
    t = Z + M.encode("utf-8").hex()
    tt = bin(int(t, 16))[2:].zfill(len(t) * 4)
    e = sm3.hash1(tt)
    t1=(r+s)%n
    x2,y2=add(multiply(G,s,a,b,p),multiply(P,t1,a,b,p),a,b,p)
    R=(int(e,16)+x2)%n
    if r==R:
        print("True")
    else:
        print("False")