
from collections import deque


def bfs(start,end):
    visited = [-1] *100001
    parent = [-1] *100001
    
    q = deque()
    q.append(start)
    visited[start] = 0

    while q:
        cx = q.popleft()
        
        if cx == end:
            break
        else:
            for i in (cx-1,cx+1,cx*2):
                 if 0 <= i <= 100000 and visited[i] == -1:
                    q.append(i)
                    visited[i] = visited[cx] + 1
                    parent[i] = cx           
    path = []
    cur = end
    while cur != -1:
        path.append(cur)
        cur = parent[cur]
    path.reverse()
    return visited[end], path



N,K = map(int,input().split())

time,path = bfs(N,K)

print(time)
print(' '.join(map(str,path)))