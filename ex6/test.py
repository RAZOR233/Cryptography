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
def check(num):# miller_rabin
    y = num - 1
    r = 0
    if num < 2: return False
    if num < 2: return False
    small_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101,
                    103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199,
                    211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317,
                    331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443,
                    449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577,
                    587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701,
                    709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839,
                    853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983,
                    991, 997]
    if num in small_primes: return True  # 如果是小素数,那么直接返回true
    # 如果大数是这些小素数的倍数,那么就是合数,返回false
    for prime in small_primes:
        if num % prime == 0: return False

    while y % 2 == 0:
        y = y // 2
        r += 1

    for _ in range(10):
        a = random.randint(2, num - 1)
        while egcd(a, num)[2] != 1:
            a = random.randint(2, num - 1)
        x = pow(a, y, num)
        if x == 1 or x == num - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, num)
            if x == 1:
                return False
            if x == num - 1:
                break
        if x != num - 1:
            return False
    return True

def RSA(m,e,p,q):
    N=p*q
    c=twomod(m,e,N)
    return c
def RSAa(c,e,p,q):
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
count=0
i=random.randint(2**1024,2**1025)
while(check(i)==0):
    i=random.randint(2**1024,2**1025)
print("p:",i)
p=i
i=random.randint(2**1024,2**1025)
while(check(i)==0):
    i=random.randint(2**1024,2**1025)
print("q:",i)
q = i
e = random.randint(2**114,2**514)
while(egcd(e,(p-1)*(q-1))[2]!=1):
    e = random.randint(2 ** 114, 2 ** 514)
p=37
q=73
e=17
m=2039
c=RSA(m,e,p,q)
print("c:",c)
print("m:",RSAa(c,e,p,q))

