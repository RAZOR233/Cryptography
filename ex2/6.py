def num(w):
    return ord(w)-ord('a')
def encrypt(a,list):
    ans=[0 for i in range(n)]
    for i in range(0,n):
        for j in range(0,n):
            ans[i]+=list[j][i]*a[j]
            ans[i]=ans[i]%26
    return ans
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
    return(x1, y1, a)
def submatrix(A,i,j):
    #矩阵A第i行第j列元素的余矩阵
    p=len(A)#矩阵的行数
    q=len(A[0])#矩阵的列数
    C=[[A[x][y] for y in range(q) if y!=j] for x in range(p) if x!=i]#列表推导式
    return C
def det(A):
    #按第一行展开递归求矩阵的行列式
    p=len(A)#矩阵的行数
    q=len(A[0])#矩阵的列数
    if(p==1 and q==1):
        return A[0][0]
    else:
        value=0
        for j in range(q):
            value+=((-1)**(j+2))*A[0][j]*det(submatrix(A,0,j))
        return value
def INVERSE(A):
    p=len(A)#矩阵的行数
    q=len(A[0])#矩阵的列数
    C=[[0 for i in range(0,p)] for j in range(0,p)]
    d=det(A)
    for i in range(p):
        for j in range(q):
            C[i][j]=((-1)**(i+j+2))*det(submatrix(A,j,i))
            C[i][j]=C[i][j]*egcd(d,26)[0]%26
    return(C)

n=int(input())
list = [[0 for i in range(n)] for j in range(n)]
for i in range(0,n):
    list[i] = input().split()
for i in range(0,n):
    for j in range(0, n):
        list[i][j]=int(list[i][j])
t1=input()
t1=t1.strip('\n')
t1=t1.strip('\r')
mode=int(input())
a=[0 for i in range(n)]
if mode==1:
    for k in range(0,len(t1)//n):
        for i in range(0, n):
            a[i]=num(t1[k*n+i])
        ans=encrypt(a,list)
        for i in range(0,n):
            print(chr(ord('a')+ans[i]),end='')
else:
    D=INVERSE(list)
    for k in range(0, len(t1) // n):
        for i in range(0, n):
            a[i] = num(t1[k * n + i])
        ans = encrypt(a, D)
        for i in range(0, n):
            print(chr(ord('a') + ans[i]), end='')