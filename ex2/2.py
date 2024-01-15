t1=input()
t2=input()
s=input()
mode=int(input())
for p in s:
    if mode==1:
        print(t2[t1.index(p)],end='')
    else:
        print(t1[t2.index(p)], end='')