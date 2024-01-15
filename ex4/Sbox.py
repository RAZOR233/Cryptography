poly=0x11b
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
def exEuclid(a, b):
    if b == 0:
        return (1, 0, a)
    x1 = 1
    y1 = 0
    x2 = 0
    y2 = 1
    while b != 0:
        q =divide(a , b)
        r = mod(a ,b)
        a = b
        b = r
        x = x1 ^ multiply(q,x2)
        x1 = x2
        x2 = x
        y = y1 ^ multiply(q,y2)
        y1 = y2
        y2 = y
    return(x1, y1, a)
def inverse(a):
    return exEuclid(a,poly)[0]
def output(S):
    for i in range(0,16):
        for j in range(0,16):
            print("0x"+'{:02x}'.format(S[i][j]),end=' ')
        print('\n',end='')
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
def quwei(b,i):
    return b>>i&1
def change(b):
    out=0
    c = 0x63
    for i in range(0, 8):
        #print(quwei(b, i), (quwei(b, i % 8) ^ quwei(b, (i + 4) % 8) ^ quwei(b, (i + 5) % 8) ^ quwei(b, (i + 6) % 8) ^ quwei(b, (i + 7) % 8) ^ quwei(c, i)))
        out += (quwei(b, i) ^ quwei(b, (i + 4) % 8) ^ quwei(b, (i + 5) % 8) ^ quwei(b, (i + 6) % 8) ^ quwei(b, (i + 7) % 8) ^ quwei(c, i)) << i
    return out
def nichange(b):
    out=0
    d = 0x05
    for i in range(0, 8):
        out += (quwei(b, (i + 2) % 8) ^ quwei(b, (i + 5) % 8) ^  quwei(b, (i + 7) % 8) ^ quwei(d, i)) << i
    return out
Sbox=[[i+j*16 for i in range(0,16)] for j in range(0,16)]
S1=[[i+j*16 for i in range(0,16)] for j in range(0,16)]
S2=[[i+j*16 for i in range(0,16)] for j in range(0,16)]
S3=[[i+j*16 for i in range(0,16)] for j in range(0,16)]
output(Sbox)
#求逆运算
for i in range(0, 16):
    for j in range(0, 16):
        if i==0 and j==0:
            S1[i][j]=0
        else:
            S1[i][j]=inverse(Sbox[i][j])
output(S1)
# print("\n")
#字节变换
for i in range(0, 16):
    for j in range(0, 16):
        S2[i][j]=change(S1[i][j])
output(S2)
# print("\n")
# #逆变换
for i in range(0, 16):
    for j in range(0, 16):
        S3[i][j]=inverse(nichange(Sbox[i][j]))
output(S3)