import sha1
ipad = 0x36363636363636363636363636363636363636363636363636363636363636363636363636363636363636363636363636363636363636363636363636363636
opad = 0x5c5c5c5c5c5c5c5c5c5c5c5c5c5c5c5c5c5c5c5c5c5c5c5c5c5c5c5c5c5c5c5c5c5c5c5c5c5c5c5c5c5c5c5c5c5c5c5c5c5c5c5c5c5c5c5c5c5c5c5c5c5c5c5c

def padding(K,pad):
    temp=K
    while len(temp)<128:
        temp=temp+'0'
    t=int("0x"+temp,16)^pad
    return t
def hash1(K,m):
    K1 = padding(K,ipad)
    t1 = hex(K1)[2:]
    text = '0b' + sha1.str_2_bin(m)
    t2 = hex(int(text, 2))[2:]
    H = t1 + t2
    # print(H)
    result = sha1.Hash1(H)
    return result
def hash2(K,m):
    K2=hex(padding(K,opad))[2:]
    t2=hex(m)[2:]
    temp=K2+t2
    result = sha1.Hash1(temp)
    return result
K=input()
m=input()
t=hash1(K,m)
# print(t)
out=hash2(K,t)
print(hex(out))
