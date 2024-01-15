n=int(input())
t1=input()
t1=t1.strip('\n')
t1=t1.strip('\r')

mode=int(input())
if mode==1:
    k = len(t1) // n + (len(t1) % n !=0)
    for i in range(0,n):
        for p in range(0,k):
            if(p*n+i<len(t1)):
                print(t1[p*n+i],end='')
else:
    k = len(t1) // n
    for i in range(0,k):
        for p in range(0,n):
            if p*(k)+i+min(len(t1) % n,i)<len(t1):
                print(t1[p*(k)+i+min(len(t1) % n,p)],end='')
    if len(t1)%n!=0:
        i=k
        for p in range(0,len(t1)%n):
            print(t1[p*(k)+i+min(len(t1) % n,p)],end='')