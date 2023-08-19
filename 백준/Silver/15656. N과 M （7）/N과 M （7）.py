


def dfs(n,tlst):

    if n == M:
        ans.append(tlst)
        return


    for j in range(N):                
        dfs(n+1,tlst+[arr[j]])
        





N,M = map(int,input().split())
arr=list(map(int,input().split()))
ans = []
v=[0]*N
dfs(0,[])
ans.sort()
for i in ans:
    print(*i)