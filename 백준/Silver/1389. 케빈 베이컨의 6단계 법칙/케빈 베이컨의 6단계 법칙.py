from collections import deque
import sys 

input = sys.stdin.readline


def bfs(i):
    visited = [0]*(n+1)
    queue = deque()
    queue.append(i)
    visited[i]=1
    while queue:
        t = queue.popleft()
        for j in arr[t]:
            if not visited[j]:
                visited[j] = visited[t]+1
                queue.append(j)
    return sum(visited)


n,m  = map(int,input().split())

arr = [[] for _ in range(n+1)]
for _ in range(m):
    x,y = map(int,input().split())
    arr[x].append(y)
    arr[y].append(x)

res =[]
for i in range(1,n+1):
    res.append(bfs(i))
print(res.index(min(res))+1)







