
from collections import deque


def bfs(z,x,y):
    q = deque()
    q.append((z,x,y))
    visited[z][x][y] = 1

    while q:
        cz,cx,cy = q.popleft()
        for i in range(6):
            nz = cz + dz[i]
            nx = cx + dx[i]
            ny = cy + dy[i]
            if 0<=nz<L and 0<=nx<R and 0 <= ny < C:
                if visited[nz][nx][ny] == 0 and arr[nz][nx][ny] == '.':
                    q.append((nz,nx,ny))
                    visited[nz][nx][ny] = visited[cz][cx][cy] +1
                elif arr[nz][nx][ny] == 'E':
                    return visited[cz][cx][cy]
    return -1


dz = [0,0,0,0,-1,1]
dx = [-1,1,0,0,0,0]
dy = [0,0,-1,1,0,0]

while True:
    L,R,C = map(int,input().split())
    if L == 0 and R == 0 and C == 0:
        break
    arr = []
    for _ in range(L):
        arr.append([list(map(str,input().strip())) for _ in range(R)])
        cnt = input()
    
    visited = [[[0] * C for _ in range(R)] for _ in range(L)]

    for i in range(L):
        for j in range(R):
            for k in range(C):
                if arr[i][j][k] == 'S':
                    ans = bfs(i,j,k)
                    if ans == -1:
                        print('Trapped!')
                    else:
                        print(f"Escaped in {ans} minute(s).")