

from collections import deque


def bfs(x,y):
    q = deque()
    q.append((x,y))
    graph[x][y] = 0 # 방문 처리를 위해 0으로 변경
    cnt = 1
    while q:
        cx,cy = q.popleft()
        for i in range(4):
            nx = dx[i] + cx
            ny = dy[i] + cy
            if 0<=nx< n and 0 <= ny < m and graph[nx][ny] == 1:
                cnt +=1
                q.append((nx,ny))
                graph[nx][ny] = 0

    return cnt


dx = [-1,1,0,0]
dy = [0,0,-1,1]
n,m,k = map(int,input().split())

graph = [[0]* m for _ in range(n)]

for _ in range(k):
    r,c = map(int,input().split())
    graph[r-1][c-1] = 1

ans = 0

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            ans = max(bfs(i,j),ans)
print(ans)