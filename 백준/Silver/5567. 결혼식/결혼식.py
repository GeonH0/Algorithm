import imp


import sys
from collections import defaultdict,deque


def bfs(start):
    cnt =0
    visited =[0 for _ in range(n+1)]
    visited[start]=1
    queue = deque([[start,0]])    
    while queue:
        u,dist = queue.popleft()
        if dist<=2:
            cnt +=1
        for v in g[u]:
            if not visited[v]:
                visited[v]=1
                queue.append([v,dist+1])
    return cnt -1
n = int(input().strip())
m = int(input().strip())
g= defaultdict(list)
for _ in range(m):
    a,b = map(int,input().split())
    g[a].append(b)
    g[b].append(a)
print(bfs(1))