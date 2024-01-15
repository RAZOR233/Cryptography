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
def ch(a1,a2,a3,b1,b2,b3):
    m=a1*a2*a3
    m1=m//a1
    m2 = m//a2
    m3 = m//a3

    t1=egcd(m1,a1)[0]
    t2 = egcd(m2, a2)[0]
    t3 = egcd(m3, a3)[0]
    print(m,t1,t2,t3)
    x=(b1*t1*m1+b2*t2*m2+b3*t3*m3)%m
    if x - m > 0:
        x = x % m

    while x <= 0:
        x += abs(m)

    return x
a1, a2 ,a3= map(int, input().split())
b1, b2 ,b3= map(int, input().split())
print(ch(a1,a2,a3,b1,b2,b3))