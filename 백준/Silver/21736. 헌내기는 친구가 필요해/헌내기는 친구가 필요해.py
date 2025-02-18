
from collections import deque
import sys


def bfs(x,y):
    q = deque()
    q.append((x,y))
    visited[x][y] = 1
    cnt = 0
    while q:
        cx,cy = q.popleft()
        for i in range(4):
            nx = dx[i] + cx
            ny = dy[i] + cy
            if 0<=nx<N and 0<= ny < M and visited[nx][ny] == 0 and arr[nx][ny] != 'X':
                q.append((nx,ny))
                visited[nx][ny] = 1
                if arr[nx][ny] == 'P':
                    cnt +=1

    return cnt
        

dx = [-1,1,0,0]
dy = [0,0,-1,1]

input = sys.stdin.readline

N,M = map(int,input().split())

arr = [list(input().strip()) for _ in range(N)]

visited= [[0]*M for _ in range(N)]

for i in range(N):
    for j in range(M):
        if arr[i][j] == "I":            
            ans = bfs(i,j)

print("TT" if ans == 0 else ans)