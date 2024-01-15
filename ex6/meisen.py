w, n, m, r = 32, 624, 397, 31
a = 0x9908b0df
f = 0x6c078965
u, d = 11, 0xffffffff
s, b = 7, 0x9d2c5680
t, c = 15, 0xefc60000
l = 18
mt=[0 for i in range(n)]
def Initialize(seed):
    mt[0]=seed
    for i in range(1,n):
        mt[i] = (f * (mt[i - 1] ^ (mt[i - 1] >> 30)) + i)& 0xffffffff
def twist():
    tmp=0
    for i in range(r):
        tmp=(tmp<<1)+1
    for i in range(n):
        x=((mt[i]>>r)<<r)+(mt[(i+1)%n]&tmp)
        xa=x>>1
        if x%2!=0:
            xa=xa^a
        mt[i] = mt[(i + m) % n] ^ xa
seed=int(input())
Initialize(seed)
twist()
for i in range(20):
    y=mt[i]
    y ^= (y >> u)
    y ^= (y << s) & b
    y ^= (y << t) & c
    y ^= (y >> l)
    print(y)