import gmpy2
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
p=int(input())
a=int(input())
b=int(input())
x,y= map(str, input().split())
G=[int(x),int(y)]
Xa=int(input())
x,y= map(str, input().split())
Y=[int(x),int(y)]
K=multiply(Y,Xa,a,b,p)
print(K[0], K[1])