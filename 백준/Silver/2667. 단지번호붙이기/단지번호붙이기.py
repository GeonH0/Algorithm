
from collections import deque


def bfs(x,y):
    q = deque()
    q.append((x,y))
    cnt = 1 # 집의 총 갯수
    visited[x][y] = 1 # 방문처리

    while q:
        cx,cy = q.popleft()
        for i in range(4):
            nx = dx[i] + cx
            ny = dy[i] + cy

            if 0<= nx < N and 0 <= ny < N and graph[nx][ny] == 1 and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                q.append((nx,ny))
                cnt +=1
    return cnt



dx = [-1,1,0,0]
dy = [0,0,-1,1]

N = int(input())

graph = [ list(map(int,input())) for _ in range(N)]
visited = [[0]*N for _ in range(N)]

dan_cnt = 0
dan_size = []
for i in range(N):
    for j in range(N):
        if graph[i][j] == 1 and visited[i][j] == 0:            
            dan_size.append(bfs(i,j))
            dan_cnt +=1

print(dan_cnt)
dan_size.sort()
for i in dan_size:
    print(i)