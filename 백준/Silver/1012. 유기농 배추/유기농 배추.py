
from collections import deque


def bfs(x,y):
    q = deque()
    q.append((x,y))
    graph[x][y] = 0

    while q:
        cx,cy = q.popleft()
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]

            if 0<=nx<N and 0 <= ny <M:
                if graph[nx][ny] == 1:
                    q.append((nx,ny))
                    graph[nx][ny] = 0
    return
                

    



T = int(input())

dx = [-1,1,0,0]
dy = [0,0,-1,1]

ans = []
for _ in range(T):

    M,N,K = map(int,input().split())
    graph = [[0]*M for _ in range(N)]
    
    for j in range(K):
        x,y = map(int,input().split())
        graph[y][x] = 1
    cnt = 0

    for i in range(N):
        for j in range(M):
            if graph[i][j] == 1:
                bfs(i,j)
                cnt += 1
    print(cnt)

