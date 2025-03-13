from collections import deque
import sys


def check(x):
    visited =[[False] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if arr[i][j] <= x:
                visited[i][j] = True
    return visited


def bfs(x,y,visited):
    q = deque()
    q.append((x,y))
    visited[x][y] = True

    while q:
        cx,cy= q.popleft()
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if 0<=nx<N and 0<=ny<N and not visited[nx][ny]:
                visited[nx][ny] = True
                q.append((nx,ny))
                

    

dx = [-1,1,0,0]
dy = [0,0,-1,1]    

input = sys.stdin.readline


N = int(input())
arr = []
for _ in range(N):
    arr.append(list(map(int,input().split())))

ans = 0

min_height = min(map(min, arr))
max_height = max(map(max, arr))

for k in range(min_height-1,max_height+1):    
    visited = check(k)    
    cnt = 0 # 안전 지대 count
    
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:                
                bfs(i,j,visited)
                cnt +=1
    ans = max(ans,cnt)

print(ans)
            
