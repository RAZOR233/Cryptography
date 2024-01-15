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
    if a < 0:
        a = -1 * a
        x1 = -1 * x1
        y1 = -1 * y1
    while x1 < 0:
        if(x2>0):
            x1=x2 +x1
            y1=y2 +y1
        else:
            x1 = x1 - x2
            y1 = y1 -y2
    while (x1-abs(x2)) > 0:
        if(x2<0):
            x1=x2 +x1
            y1=y2 +y1
        else:
            x1 = x1 - x2
            y1 = y1 -y2
    return(x1, y1, a)
def encode(p,k,b):
    return chr(ord('a')+((ord(p)-ord('a'))*k+b)%26)
def decode(p,k,b):
    return chr(ord('a') + (((ord(p) - ord('a')) - b)  * f) % 26)
k, b = map(int, input().split())
a=input()
s=a.strip('\n')
s=s.strip('\r')
mode=int(input())
if egcd(k,26)[2]!=1:
    print("invalid key")
else:
    for p in s:
        if mode==1:
            print(encode(p,k,b),end='')
        else:
            f=egcd(k,26)[0]
            print(decode(p,k,b), end='')
