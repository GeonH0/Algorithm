import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n,m,r = map(int,input().split())
graph =[[]for _ in range(n+1)]
visited=[False]*(n+1)
answer=[0]*(n+1)
cnt=1

def dfs(v):
    global cnt
    visited[v]=True
    answer[v]=cnt
    graph[v].sort(reverse=True)
    for i in graph[v]:
        if not visited[i]:
            cnt+=1
            dfs(i)


for _ in range(m):
    x,y = map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)

dfs(r)
for j in answer[1:]:
    print(j)




