
from collections import deque


def bfs():
    global k
    q = deque()
    q.append((0,0,0,0))
    visited[0][0][0] = True

    while q:
        cx,cy,horse,now = q.popleft()
        if cx == H -1 and cy == W-1:
            return now
        if horse < k:
            for i in range(8):
                nx = cx + horsex[i]
                ny = cy + horsey[i]
                if 0<= nx < H and 0 <= ny < W:
                    if arr[nx][ny] == 0 and not visited[nx][ny][horse+1]:
                        visited[nx][ny][horse+1] = True
                        q.append((nx,ny,horse+1,now+1))
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if 0<=nx < H and 0 <= ny < W:
                if arr[nx][ny] == 0 and not visited[nx][ny][horse]:
                    visited[nx][ny][horse] = True
                    q.append((nx,ny,horse,now+1))
    return -1

        
    

dx = [-1,1,0,0]
dy = [0,0,-1,1]
horsex = [-1, 1, 2, 2, 1, -1, -2, -2]
horsey = [2, 2, 1, -1, -2, -2, -1, 1]
k = int(input())
W,H = map(int,input().split())
visited = [[[False]*(k+1) for _ in range(W)] for _ in range(H)]
arr = [list(map(int,input().split())) for _ in range(H)]

print(bfs())