n=int(input())
l = list(range(1,n+1))
l[0] = 0
for i in range(2,n+1):
    if l[i-1] != 0 :
        print(i, end=" ")
        for j in range(i*2,n+1,i):
            l[j-1] = 0
