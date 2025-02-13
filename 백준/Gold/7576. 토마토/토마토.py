
from collections import deque


def bfs():
    time = 0
    while q:
        cx,cy,ct = q.popleft()
        time = max(ct,time)
        for i in range(4):
            nx = dx[i] + cx
            ny = dy[i] + cy
            if 0<=nx<N and 0<=ny<M and graph[nx][ny] == 0:
                q.append((nx,ny,time+1))                
                graph[nx][ny] = 1
    return time
                
    
                
dx = [-1,1,0,0]
dy = [0,0,-1,1]
M,N = map(int,input().split())

graph = [list(map(int,input().split())) for _ in range(N)]
q = deque()

for i in range(N):
    for j in range(M):
        if graph[i][j] == 1:
            q.append((i,j,0))

result= bfs()
for i in range(N):
    for j in range(M):
        if graph[i][j] == 0:
            print(-1)
            exit()
print(result)
           
            
