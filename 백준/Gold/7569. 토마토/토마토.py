
from collections import deque



def bfs():
    while tomato_queue:
        cz,cx,cy = tomato_queue.popleft()
        for i in range(6):
            nx = cx + dx[i]
            ny = cy + dy[i]
            nz = cz +dz[i]
            if 0<=nx < N and 0<=ny < M and 0<=nz < H:
                if arr[nz][nx][ny] == 0: # 범위 안에 있으면서 0 일경우
                    arr[nz][nx][ny] = arr[cz][cx][cy] +1
                    tomato_queue.append((nz,nx,ny))

        


M,N,H =map(int,input().split())
dx = [-1,1,0,0,0,0]
dy = [0,0,-1,1,0,0]
dz = [0,0,0,0,-1,1]

arr = []
for _ in range(H):
    arr.append([list(map(int,input().split())) for _ in range(N)])

tomato_queue = deque()

for k in range(H):
    for i in range(N):
        for j in range(M):
            if arr[k][i][j] == 1:
                tomato_queue.append((k,i,j))

bfs()

if any(0 in row for floor in arr for row in floor):
    print(-1)
else:
    max_days = max(max(row) for floor in arr for row in floor)
    if max_days == 1:
        print(0)
    else:
        print(max_days - 1)