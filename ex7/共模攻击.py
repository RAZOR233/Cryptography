import gmpy2
def egcd(a, b):
    #a*xi + b*yi = ri
    if b == 0:
        return (1, 0, a)
    #a*x1 + b*y1 = a
    x1 = 1
    y1 = 0
    #a*x2 + b*y2 = b
    x2 = 0
    y2 = 1
    while b != 0:
        q =int(a // b)
        #ri = r(i-2) % r(i-1)
        r = a % b
        a = b
        b = r
        #xi = x(i-2) - q*x(i-1)
        x = x1 - q*x2
        x1 = x2
        x2 = x
        #yi = y(i-2) - q*y(i-1)
        y = y1 - q*y2
        y1 = y2
        y2 = y
    return(x1, y1)
# def egcd(a, b):
#     u1, v1, r1 = 1, 0, a
#     u2, v2, r2 = 0, 1, b
#     while r2 != 1:
#         k = r1 // r2
#         m = r1 % r2
#         u3, v3, r3 = u2, v2, r2
#         u2 = u1 - k * u2
#         v2 = v1 - k * v2
#         r2 = r1 - k * r2
#         u1, v1, r1 = u3, v3, r3
#     return u2, v2
def twomod(b, e, m):
    result = 1
    while e != 0:
        if (e&1) == 1:
            # ei = 1, then mul
            result = (result * b) % m
        e >>= 1
        # b, b^2, b^4, b^8, ... , b^(2^n)
        b = (b*b) % m
    return result
e1=int(input())
e2=int(input())
c1=int(input())
c2=int(input())
N=int(input())
s1,s2=egcd(e1,e2)
# print(twomod(c1,s1,N)*twomod(c2,s2,N))
print(gmpy2.powmod(c1,s1,N)*gmpy2.powmod(c2,s2,N)%N)