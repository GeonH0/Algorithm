


def dfs(n,tlst):

    #종료 조건
    if n== M:
        ans.append(tlst)
        return

    for j in range(0,N):
        if v[j]==0:
            v[j]=1
            dfs(n+1,tlst+[arr[j]])
            v[j]=0 # 원상 복구







N,M = map(int,input().split())
arr=list(map(int,input().split()))
arr.sort()
ans = []
v=[0]*(N+1)
dfs(0,[])
for i in ans:
    print(*i)