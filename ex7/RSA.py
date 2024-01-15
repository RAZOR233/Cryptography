import random
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

def encrypt(m,e,p,q):
    N=p*q
    c=twomod(m,e,N)
    return c
def decrypt(c,e,p,q):
    (x,y,z)=egcd((p-1)*(q-1),e)
  #  print(x,y,z)
    d=int(y)
    print("d:",d)
    if(d<0):
        d=d+(p-1)*(q-1)
    # m1=((c%p)**(d%(p-1)))%p
    m1=twomod(c%p,d%(p-1),p)
    #m2 = ((c % q) ** (d % (q - 1))) % q
    m2 = twomod(c % q, d % (q - 1), q)
    A=egcd(q,p)[0]
    B=egcd(p,q)[0]
    m=(m1*A*q+m2*B*p)%(p*q)
    return m
p=int(input())
q=int(input())
e=int(input())
m=int(input())
op=int(input())
if op==1:
    print(encrypt(m,e,p,q))
else :
    print(decrypt(m,e,p,q))