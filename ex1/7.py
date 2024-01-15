poly=int('0x11b',16)
def mod(a,b):
    ans=0
    rec=0
    la=str(bin(a))
    lb=str(bin(b))
    while len(la)>len(lb)-1:
        rec=len(la)-len(lb)
        a^=(b<<rec)
        ans^=(1<<rec)
        la = str(bin(a))
        lb = str(bin(b))
    #print(ans,hex(a))
    return a
def multiply(a,b):
    ans=0
    while b>0:
        if b&1==1:
            ans^=a
        a<<=1
        if a&int('0x100',16)==int('0x100',16):
            a^=poly
        a&=int('0xff',16)
        b>>=1
    return ans
def fastmod(b,e,m):
    result = 1
    while e != 0:
        if (e & 1) == 1:
            # ei = 1, then mul
            #result = (result * b) % m
            result = mod(multiply(result,b),m)
        e >>= 1
        # b, b^2, b^4, b^8, ... , b^(2^n)
        #b = (b * b) % m
        b = mod(multiply(b, b), m)
    return result
m=int("0x11b",16)
a,b = map(str, input().split())
c=int(a,16)
e=int(b)
ans=str(hex(fastmod(c,e,poly)))
print(ans[2],end='')
print(ans[3],end='')

