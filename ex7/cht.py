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
    return(x1, y1, a)
def cht(a,m):
    M=1
    for k in m:
        M=M*k
    x=0
    for i in range(len(a)):
        t=egcd((M//m[i]),m[i])[0]
        x=(x+a[i]*t*(M//m[i]))%M
    return x
m=[23,28,33]
a=[1,2,3]
print(cht(a,m))
