def num(w):
    return ord(w)-ord('a')
t1=input()
t2=input()
t1=t1.strip('\n')
t1=t1.strip('\r')
t2=t2.strip('\n')
t2=t2.strip('\r')
mode=int(input())
i=0
if mode==1:
    for p in t2:
        if(i==len(t1)):
            i=0
        print(chr(ord('a')+(num(p)+num(t1[i]))%26),end='')
        i+=1
else:
    for p in t2:
        if(i==len(t1)):
            i=0
        print(chr(ord('a')+(num(p)-num(t1[i]))%26),end='')
        i += 1