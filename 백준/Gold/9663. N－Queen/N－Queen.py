

def dfs(n):
    global cnt
    if n == N:
        cnt +=1 #경우의수 추가
        return
    for i in range(0,N):
        if v1[i] ==0 and v2[i+n]==0 and v3[i-n]==0:
            v1[i] =v2[i+n]=v3[i-n]  =1
            dfs(n+1)
            v1[i] =v2[i+n]=v3[i-n]  = 0





N = int(input())
cnt=0

v1=[0]*N
v2=[0]*(2*N)
v3=[0]*(2*N)
dfs(0)
print(cnt)

