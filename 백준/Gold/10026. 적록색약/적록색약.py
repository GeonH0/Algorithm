

from collections import deque
import sys


def bfs(x,y,color,mod):
    q = deque()
    q.append((x,y))
    if mod == 0:
        visited[x][y] = 1
    else:
        visitedR[x][y] = 1
    
    while q:
        cx,cy = q.popleft()
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if 0<=nx<N and 0<=ny<N:
                if mod == 0: # 적록색약이 아닐경우
                    if arr[nx][ny] == color and visited[nx][ny] == 0:                
                        visited[nx][ny] = 1
                        q.append((nx,ny))
                else:
                    if (color == 'R' or color == 'G'): # 현재 색상이 빨강이거나 초록일떄
                        if (arr[nx][ny] == 'R' or arr[nx][ny] == 'G') and visitedR[nx][ny] == 0:
                            visitedR[nx][ny] = 1
                            q.append((nx,ny))
                    elif arr[nx][ny] == color and visitedR[nx][ny] == 0:
                        visitedR[nx][ny] = 1
                        q.append((nx,ny))

                                    
                    
dx = [-1,1,0,0]
dy = [0,0,-1,1]

input = sys.stdin.readline

N = int(input())

arr = [list(map(str,input().strip())) for _ in range(N)]
visited =[[0]*N for _ in range(N)]
visitedR = [[0]*N for _ in range(N)]
ans1,ans2 = 0,0

# 일반인 BFS 탐색
for i in range(N):
    for j in range(N):
        if visited[i][j] == 0:
            bfs(i, j, arr[i][j], 0)
            ans1 += 1

# 적록색약 BFS 탐색
for i in range(N):
    for j in range(N):
        if visitedR[i][j] == 0:
            bfs(i, j, arr[i][j], 1)
            ans2 += 1



print(ans1,ans2)
            
            
