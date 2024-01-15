
l=int(input())
p=int(input())
q=int(input())
s=int(input())
n=p*q
x=(s*s)%n
ans=[]
out=0
for i in range(l):
    x=(x*x)%n
    # print(x)
    ans.append(x%2)
    # ans=(ans<<1)+(x%2)
# print(bin(ans))
for i in range(len(ans)):
    out = (out << 1) + ans[len(ans)-1-i]
print(out)