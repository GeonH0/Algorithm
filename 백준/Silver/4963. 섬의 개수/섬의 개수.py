

from collections import deque


def bfs(x,y):
    q = deque()
    q.append((x,y))
    arr[x][y] = 0

    while q:
        cx,cy = q.popleft()
        for i in range(8):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if 0 <= nx < w and 0 <= ny < h and arr[nx][ny] == 1:
                q.append((nx,ny))
                arr[nx][ny] = 0             





dx = [-1,1,0,0,1,-1,1,-1]
dy = [0,0,-1,1,1,1,-1,-1]
ans = []

while True:
    h,w = map(int,input().split())    
    if w == 0 and h == 0:
        break
    else:        
        arr = [list(map(int,input().split())) for _ in range(w)]
        cnt = 0
        for i in range(w):
            for j in range(h):
                if arr[i][j] == 1:
                    bfs(i,j)
                    cnt += 1
        ans.append(cnt)

for i in ans:
    print(i)
        


