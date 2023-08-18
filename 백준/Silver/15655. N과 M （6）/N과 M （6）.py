

def dfs(n,s,tlst):

    if n ==M:
        ans.append(tlst)
        return

    for j in range(s,N):
        if v[j]==0:
            v[j]=1
            dfs(n+1,j+1,tlst+[arr[j]])
            v[j]=0

        





N,M = map(int,input().split())


arr=list(map(int,input().split()))
arr.sort()
ans =[]
v=[0]*(N+1)


dfs(0,0,[])
ans.sort()
for i in ans:
    print(*i)