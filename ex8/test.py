import gmpy2
def multiply(Q,n, a,b,p):
    result = [0, 0]
    while n > 0:
        if n & 1:
            result = plus(result, Q,a,b,p)
        n >>= 1
        Q = plus(Q, Q,a,b,p)
    return result


def plus(P, Q,a,b,p):
    if P[0]==Q[0] and P[1]==-Q[1]:
        return [0,0]
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
x1=int(x)
y1=int(y)
x,y= map(str, input().split())
x2=int(x)
y2=int(y)
k=int(input())
# t,tt=plus(x1,y1,x1,y1,a,b,p)
# x,y=plus(t,tt,x1,y1,a,b,p)
# i=1
# while x!=t or y!=tt:
#     x, y = plus(x, y, x1, y1, a, b, p)
#     i+=1
x,y=plus([x1,y1],[x2,y2],a,b,p)
print(x,y)
x,y=plus([x1,y1],[x2,-y2],a,b,p)
print(x,y)
x,y=multiply([x1,y1],k,a,b,p)
print(x,y)
x,y=multiply([x2,y2],gmpy2.invert(k,p),a,b,p)
print(x,y)
# print(plus(x1,y1,x1,y1,a,b,p))
# print(multiply(x1,y1,2,a,b,p))