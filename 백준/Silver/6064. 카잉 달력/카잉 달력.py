
def cal(m,n,x,y):
    while x<=m*n:
        if (x-y) % n ==0:
            return x
        x +=M
    return -1
 
T = int(input())
for _ in range(T):
    M,N,x,y = map(int,input().split())
    print(cal(M,N,x,y))