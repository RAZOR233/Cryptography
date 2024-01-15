n=int(input())
t1=input()
t2=input()
t1=t1.strip('\n')
t1=t1.strip('\r')
t2=t2.strip('\n')
t2=t2.strip('\r')
mode=int(input())
list=[0 for i in range(0,len(t1))]
for i in range(0,len(t1)):
    list[i]=int(t1[i])
k=len(t2)//n
if mode==1:
    for i in range(0, n):
        for j in range(0, k):
            print(t2[list.index(i + 1) + j * n], end='')
else:
    for j in range(0, k):
        for i in range(0, n):
            print(t2[(list[i]-1)*k + j] , end='')
