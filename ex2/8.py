def max(list):
    max=-1
    num=0
    for i in range(0,len(list)):
        if max<list[i]:
            max=list[i]
            num=i
    if max!=-1:
        return num
    else:
        return -1
def num(w):
    return ord(w)-ord('a')
def egcd(a, b):
    #a*xi + b*yi = ri
    if b == 0:
        return (1, 0, a)
    #a*x1 + b*y1 = a
    x1 = 1
    y1 = 0
    #a*x2 + b*y2 = b
    x2 = 0
    y2 = 1
    while b != 0:
        q =int(a // b)
        #ri = r(i-2) % r(i-1)
        r = a % b
        a = b
        b = r
        #xi = x(i-2) - q*x(i-1)
        x = x1 - q*x2
        x1 = x2
        x2 = x
        #yi = y(i-2) - q*y(i-1)
        y = y1 - q*y2
        y1 = y2
        y2 = y
    if a < 0:
        a = -1 * a
        x1 = -1 * x1
        y1 = -1 * y1
    while x1 < 0:
        if(x2>0):
            x1=x2 +x1
            y1=y2 +y1
        else:
            x1 = x1 - x2
            y1 = y1 -y2
    while (x1-abs(x2)) > 0:
        if(x2<0):
            x1=x2 +x1
            y1=y2 +y1
        else:
            x1 = x1 - x2
            y1 = y1 -y2
    return(x1, y1, a)
list=[0 for i in range(0,26)]
decrypt=[0 for i in range(0,26)]
t1=input()
t1=t1.strip('\n')
t1=t1.strip('\r')
list2="etaoinshrdlcumwfgypbvkjxqz"
for p in t1:
    list[num(p)]+=1
y1=max(list)
list[y1]=-1
#print(chr(ord('a')+y1))
y2=max(list)
list[y2]=-1
x1=num('e')
x2=num('t')
#print(y1,y2,x1,x2)
#print(chr(ord('a')+y2))
k=(y1-x1)%26
#k=(y1-y2)*egcd(x1-x2,26)[0]%26
print(k)
#or i in range(0,26):
    #k=max(list)
    #print(k)
    #decrypt[k]=list2[i]
    #list[k]=-1
#for p in t1:
    #print(decrypt[num(p)],end='')