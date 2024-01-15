import gmpy2
import hashlib

p=int(input())
q=int(input())
g=int(input())
M=input()
mode=input()
if mode=="Sign":
    x = int(input())
    k = int(input())
    r=gmpy2.powmod(g,k,p)
    m=bytes(M, encoding="utf-8")+str(r).encode("utf8")
    e=hashlib.sha1(m).hexdigest()
    s=(k+x*int(e,16))%q
    print(int(e,16),s)
else:
    y = int(input())
    e, s = map(int, input().split())
    r=(gmpy2.powmod(g,s,p)*gmpy2.powmod(y,e,p))%p
    t = bytes(M, encoding="utf-8") + str(r).encode("utf8")
    m=hashlib.sha1(t).hexdigest()
    if int(m,16)==e:
        print("True")
    else:
        print("False")
