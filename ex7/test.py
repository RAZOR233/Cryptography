import gmpy2
e=int(input())
d=int(input())
N=int(input())
k=((e*d-1)//N)
while((e*d-1)%k!=0):
    k+=1

t=((e*d-1)//k-N-1)*(-1)
p=(t+gmpy2.iroot(t*t-4*N,2)[0])//2
q=(t-gmpy2.iroot(t*t-4*N,2)[0])//2
if p<q:
    print(p)
    print(q)
else:
    print(q)
    print(p)