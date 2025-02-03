

from collections import deque


def dfs(graph,v,visited):
    visited[v] = True
    print(v, end = " ")
    for i in graph[v]:
        if not visited[i]:
            dfs(graph,i,visited)

def bfs(graph,start,visited):
    q = deque([start])
    visited[start] = True

    while q:
        v = q.popleft()
        print(v, end = " ")
        for i in graph[v]:
            if not visited[i]:
                q.append(i)
                visited[i] = True
    

N,M,V = map(int,input().split())
graph = [[]for _ in range(N+1)]

for _ in range(M):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, N+1):
    graph[i].sort()
    
visited = [False] * (N+1)
dfs(graph,V,visited)
print()
visited = [False] * (N+1)
bfs(graph,V,visited)
