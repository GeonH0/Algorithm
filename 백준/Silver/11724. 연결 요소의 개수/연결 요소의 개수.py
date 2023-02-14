import sys
sys.setrecursionlimit(5000)


def dfs(v):
    visited[v]=True
    for k in arr[v]:
        if not visited[k]:
            dfs(k)

n,m = map(int,input().split())
arr=[[]for _ in range(n+1)]
visited =[False]*(n+1)
cnt =0



for _ in range(m):
    u,v = map(int,input().split())
    arr[u].append(v)
    arr[v].append(u)

for i in range(1,n+1):
    if not visited[i]:
        dfs(i)
        cnt +=1

print(cnt)
