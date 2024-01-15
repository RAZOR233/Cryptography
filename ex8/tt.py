#
# hash3=hashlib.sha256()#不同算法，hashlib很多加密算法
# hash3.update(int.to_bytes(155,10,byteorder='big'))
# print(int(hash3.hexdigest(),16))
from random import randint
import math
# from prime import modinv
# from sm3 import sm3hash
import hashlib
import gmpy2
def addition(x1,y1,x2,y2,a,p):
    if x1==x2 and y1==p-y2:
        return False
    if x1!=x2:
        lamda=((y2-y1)*gmpy2.invert(x2-x1, p))%p
    else:
        lamda=(((3*x1*x1+a)%p)*gmpy2.invert(2*y1, p))%p
    x3=(lamda*lamda-x1-x2)%p
    y3=(lamda*(x1-x3)-y1)%p
    return x3,y3

def mutipoint(x,y,k,a,p):
    k=bin(k)[2:]
    qx,qy=x,y
    for i in range(1,len(k)):
        qx,qy=addition(qx, qy, qx, qy, a, p)
        if k[i]=='1':
            qx,qy=addition(qx, qy, x, y, a, p)
    return qx,qy

def kdf(z,klen):
    ct=1
    k=''
    for _ in range(math.ceil(klen/256)):
        # k=k+sm3hash(hex(int(z+'{:032b}'.format(ct),2))[2:])
        k=k+hashlib.sha256(hex(int(z+'{:032b}'.format(ct),2))[2:].encode("utf-8")).hexdigest()
        ct=ct+1
    k='0'*((256-(len(bin(int(k,16))[2:])%256))%256)+bin(int(k,16))[2:]
    return k[:klen]

#parameters
p=0x60275702009245096385686171515219896416297121499402250955537857683885541941187
a=0x54492052985589574080443685629857027481671841726313362585597978545915325572248
b=0x45183185393608134601425506985501881231876135519103376096391853873370470098074
gx=0x429905514254078361236418469080477708234343499662916671209092838329800180225085
gy=0x2940593737975541915790390447892157254280677083040126061230851964063234001314
# n=0x8542D69E4C044F18E8B92435BF6FF7DD297720630485628D5AE74EE7C32E79B7
k=0x34550576952843389977837539438321907097625575044301827052096699664811526290255
xB=0x30466142855137288468788190552058120832437161821909553502398316083968243039754
yB=0x53312363470992020232197984648603141288071418796825192480967103513769615518274
#待加密的消息M：encryption standard
#消息M的16进制表示：656E63 72797074 696F6E20 7374616E 64617264
'''
dB=0x1649AB77A00637BD5E2EFE283FBF353534AA7F7CB89463F208DDBC2920BB0DA0
xB=0x435B39CCA8F3B508C1488AFC67BE491A0F7BA07E581A0E4849A5CF70628A7E0A
yB=0x75DDBA78F15FEECB4C7895E2C1CDF5FE01DEBB2CDBADF45399CCF77BBA076A42
'''
# dB=randint(1,n-1)
# xB,yB=mutipoint(gx,gy,dB,a,p)


def encrypt(m:str):
    plen=len(hex(p)[2:])
    m='0'*((4-(len(bin(int(m.encode().hex(),16))[2:])%4))%4)+bin(int(m.encode().hex(),16))[2:]
    klen=len(m)
    x2,y2=mutipoint(xB, yB, k, a, p)
    x2,y2='{:0256b}'.format(x2),'{:0256b}'.format(y2)
    t=kdf(x2+y2, klen)
    x1,y1=mutipoint(gx, gy, k, a, p)
    x1,y1=(plen-len(hex(x1)[2:]))*'0'+hex(x1)[2:],(plen-len(hex(y1)[2:]))*'0'+hex(y1)[2:]
    c1='04'+x1+y1
    c2=((klen//4)-len(hex(int(m,2)^int(t,2))[2:]))*'0'+hex(int(m,2)^int(t,2))[2:]
    # c3=sm3hash(hex(int(x2+m+y2,2))[2:])
    c3 = hashlib.sha256(hex(int(x2+m+y2,2))[2:].encode("utf-8")).hexdigest()
    return c1,c2,c3

def decrypt(c1,c2,c3,a,b,p):
    c1=c1[2:]
    x1,y1=int(c1[:len(c1)//2],16),int(c1[len(c1)//2:],16)
    if pow(y1,2,p)!=(pow(x1,3,p)+a*x1+b)%p:
        return False
    x2,y2=mutipoint(x1, y1, dB, a, p)
    x2,y2='{:0256b}'.format(x2),'{:0256b}'.format(y2)
    klen=len(c2)*4
    t=kdf(x2+y2, klen)
    if int(t,2)==0:
        return False
    m='0'*(klen-len(bin(int(c2,16)^int(t,2))[2:]))+bin(int(c2,16)^int(t,2))[2:]
    # u=sm3hash(hex(int(x2+m+y2,2))[2:])
    u = hashlib.sha256(hex(int(x2+m+y2,2))[2:].encode("utf-8")).hexdigest()
    if u!=c3:
        return False
    return hex(int(m,2))[2:]

fstr=0x34550576952843389977837539438321907097625575044301827052096699664811526290255
print(fstr)
c1,c2,c3=encrypt(fstr)
c=(c1+c2+c3).upper()
print('\nciphertext:')
for i in range(len(c)):
    print(c[i*8:(i+1)*8],end=' ')
print('\n\nplaintext:')
'''
输出密文C= C1∥C2∥C3：
04245C26 FB68B1DD DDB12C4B 6BF9F2B6 D5FE60A3 83B0D18D 1C4144AB F17F6252
E776CB92 64C2A7E8 8E52B199 03FDC473 78F605E3 6811F5C0 7423A24B 84400F01
B8650053 A89B41C4 18B0C3AA D00D886C 00286467 9C3D7360 C30156FA B7C80A02
76712DA9 D8094A63 4B766D3A 285E0748 0653426D
'''
m1=decrypt(c1, c2, c3, a, b, p)
if m1:
    m1=str(bytes.fromhex(m1))
    m1='\n'.join(m1[2:-1].split('\\n'))
    print(m1)
    print(fstr==m1)
else:
    print(False)
