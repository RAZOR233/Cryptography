poly=int('0x11b',16)
def mod(a,b):
    ans=0
    rec=0
    la=str(bin(a))
    lb=str(bin(b))
    while len(la)>len(lb)-1 and b!=0 and a!=0:
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
def divide(a,b):
    ans=0
    rec=0
    la=str(bin(a))
    lb=str(bin(b))
    while len(la)>len(lb)-1 and b!=0 and a!=0:
        rec=len(la)-len(lb)
        a^=(b<<rec)
        ans^=(1<<rec)
        la = str(bin(a))
        lb = str(bin(b))
    #print(ans,hex(a))
    return ans
'''
def exEuclid(a1,a2):
    if(a2==0):
        return (a1,1,0)
    else:
        (GCD,xtmp,ytmp)=exEuclid(a2,mod(a1,a2))
        x=ytmp
        y=xtmp^multiply(ytmp,divide(a1,a2))
        return (GCD,x,y)'''
def exEuclid(a, b):
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
        q =divide(a , b)
        #ri = r(i-2) % r(i-1)
        r = mod(a ,b)
        a = b
        b = r
        #xi = x(i-2) - q*x(i-1)
        x = x1 ^ multiply(q,x2)
        x1 = x2
        x2 = x
        #yi = y(i-2) - q*y(i-1)
        y = y1 ^ multiply(q,y2)
        y1 = y2
        y2 = y
    return(x1, y1, a)
def output(a):
    ans = str(hex(a))
    if(len(ans)==4):
        print(ans[2], end='')
        print(ans[3], end=' ')
    else:
        print("0", end='')
        print(ans[2], end=' ')

a=int(input(),16)
a1,a2,a3=exEuclid(a,poly)
output(a1)

