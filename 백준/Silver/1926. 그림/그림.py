
from collections import deque


def bfs(x,y):
    q = deque()
    q.append((x,y))
    arr[x][y] = 0 # 방문 처리
    cnt = 1
    while q:
        cx,cy = q.popleft()
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if 0<= nx< N and 0 <= ny < M and arr[nx][ny] == 1:
                q.append((nx,ny))
                arr[nx][ny] = 0 # 해당 조건이 맞다면 방문 처리
                cnt +=1
    return cnt



dx = [-1,1,0,0]
dy = [0,0,-1,1]

N,M = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]

ans = []
for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            ans.append(bfs(i,j))

if len(ans) == 0:
    print(0)
    print(0)
else:
    print(len(ans))
    print(max(ans))