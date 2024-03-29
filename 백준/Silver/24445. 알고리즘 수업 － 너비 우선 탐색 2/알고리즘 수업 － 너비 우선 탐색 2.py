from collections import deque
import sys

input = sys.stdin.readline


n,m,r = map(int,input().split())
graph=[[]for _ in range(n+1)]
cnt=1
visited=[0]*(n+1)

for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)


def bfs(v):
    global cnt
    
    q = deque()
    q.append((r))
    visited[r]=1
    while q:
        v = q.popleft()
        graph[v].sort(reverse=True)
        for i in graph[v]:
            if visited[i]==0:
                cnt +=1
                visited[i]=cnt
                q.append(i)


bfs(r)

for i in visited[1:]:
    print(i)


    