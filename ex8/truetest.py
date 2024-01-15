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
G=[5,9]
a=1
b=6
p=11
# for i in range(2,15):
#     print(multiply(G,i,1,6,11))
print(add(multiply(G,11,a,b,p),multiply([8,3],12,a,b,p),a,b,p))