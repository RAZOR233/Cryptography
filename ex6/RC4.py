k=input()
s=int(input(),16)
Kf=[]
K=[]
j=0
T=[0 for i in range(256)]
Sbox=[i for i in range(256)]
for i in range(1,len(k)//2):
    K.append(int(k[2*i:2*i+2],16))
# while k !=0:
#     Kf.append(k&0xff)
#     k>>=8
# for i in range(len(Kf)):
# #     K.append(Kf[len(Kf)-1-i])
# for i in K:
#     print(hex(i),end='')
for i in range(256):
    T[i]=K[i%len(K)]
for i in range(256):
    j=(j+Sbox[i]+T[i])%256
    tmp=Sbox[i]
    Sbox[i]=Sbox[j]
    Sbox[j]=tmp
# for i in Sbox:
#     print(hex(i),end=' ')
i=0
j=0
flag=0
ss=str(hex(s))[2:]
if len(ss)%2!=0:
    ss="0"+ss
    flag=1
# print(ss)
print('0x',end='')
for p in range(len(ss)//2):
    i=(i+1)%256
    j=(j+Sbox[i])%256
    tmp = Sbox[i]
    Sbox[i] = Sbox[j]
    Sbox[j] = tmp
    t=(Sbox[i]+Sbox[j])%256
    t=Sbox[t]
    # if (p==len(ss)//2 -1) and flag==1:
    #     print(ss[2*p+1:2*p+2])
    #     print('{:01x}'.format((t>>4)^int(ss[2*p+1:2*p+2],16)),end='')
    # else:
    #     print(ss[2*p:2*p+2])
    print('{:02x}'.format(t^int(ss[2*p:2*p+2],16)),end='')
