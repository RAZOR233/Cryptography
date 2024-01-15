list=[2,3,7,11,13,19,29,31]
list2=[]
poly=513
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
num=0

for i in range(256,512):
    flag=0
    for k in list:
        if mod(i,k)==0:
            flag=1
    if flag==0:
        list2.append(i)
for i in list2:
    flag=0
    m=pow(2,8)-1
    f1=pow(2,m)+1
    if mod(f1,i)==0:
        flag=1
        for q in range(1,m):
            f2=pow(2,q)+1
            if mod(f2,i)==0:
                flag=0
                break
    if flag==1:
        num += 1;
        print(bin(i)[2:],end=' ')
