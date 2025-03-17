

from collections import deque


def bfs():
    q = deque()
    q.append(0)
    visited[0] = True

    while q:
        idx = q.popleft()
        x,y = location[idx]
        
        if idx == n+1:
            return 'happy'

        for i in range(n+2):
            if not visited[i]:
                nx,ny = location[i]
                if abs(nx - x) + abs(ny - y) <= 1000:  # 1000m 이내 이동 가능
                    visited[i] = True
                    q.append(i)
    return 'sad'
    



t = int(input())
for _ in range(t):
    n = int(input())
    location = []
    visited = [False] *(n+2)    
    for k in range(n+2):
        x,y = map(int,input().split())
        location.append((x,y))    
    print(bfs())
