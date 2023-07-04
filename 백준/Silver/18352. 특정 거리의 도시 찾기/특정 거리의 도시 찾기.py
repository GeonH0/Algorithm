from collections import deque
import sys
input = sys.stdin.readline


        


n,m,k,x  = map(int,input().split())




arr=[[] for _ in range(n+1)]
visited =[0]*(n+1)

for _ in range(m):
    a,b = map(int,input().split())
    arr[a].append(b)

res =[]

def bfs(x):
    queue = deque()
    queue.append(x)
    visited[x]=1

    while queue:
        t = queue.popleft()
        if visited[t] == k+1:
            res.append(t)
            continue
        for i in arr[t]:
            if visited[i] ==0:
                queue.append(i)
                visited[i] = visited[t]+1
bfs(x)
if len(res) ==0:
    print(-1)
else:
    res.sort()
    for i in res:
        print(i)
