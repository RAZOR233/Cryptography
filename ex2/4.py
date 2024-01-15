t1=input()
t2=input()
t1=t1.strip('\n')
t1=t1.strip('\r')
t2=t2.strip('\n')
t2=t2.strip('\r')
mode=int(input())
i=0
for p in t2:
    if(i==len(t1)):
        i=0
    print(chr(ord(p)^ord(t1[i])),end='')
    i+=1
