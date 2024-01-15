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
op=int(input())
if op==1:
    x, y = map(str, input().split())
    Pm = [int(x), int(y)]
    k=int(input())
    x, y = map(str, input().split())
    Pb = [int(x), int(y)]
    out1=multiply(G,k,a,b,p)
    out2=add(multiply(Pb,k,a,b,p),Pm,a,b,p)
    print(out1[0],out1[1])
    print(out2[0],out2[1])
if op==0:
    x, y = map(str, input().split())
    C1 = [int(x), int(y)]
    x, y = map(str, input().split())
    C2 = [int(x), int(y)]
    nB = int(input())
    t=multiply(C1,nB,a,b,p)
    P=add(C2,[t[0],-t[1]],a,b,p)
    print(P[0], P[1])