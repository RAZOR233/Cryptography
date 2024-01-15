poly=int('0x11b',16)
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
    return (ans,a)
x=input()
a=int(x[0],16)*16+int(x[1],16)
b=x[3]
c=int(x[5],16)*16+int(x[6],16)

if b=='+' or b=='-':
    out=a^c
elif b=='*':
    out=multiply(a,c)
else:
    out1,out=mod(a,c)
    c = str(hex(out1))
    if len(c)<4:
        print(0, end='')
        print(c[2], end='')
        print(' ', end='')
    else:
        print(c[2], end='')
        print(c[3], end='')
        print(' ', end='')

c=str(hex(out))
if len(c) < 4:
    print(0, end='')
    print(c[2], end='')
else:
    print(c[2], end='')
    print(c[3], end='')
