

from collections import deque
import sys


def bfs(x,y,ex,ey):
    dx = [-1, 1, 2, 2, 1, -1, -2, -2]
    dy = [2, 2, 1, -1, -2, -2, -1, 1]
    q = deque()
    q.append((x,y,0))
    visited[x][y] = 1
    while q:
        cx,cy,ncnt= q.popleft()
        if cx == ex and cy == ey:
            return ncnt
        for i in range(8):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if 0 <= nx < L and 0<=ny < L and visited[nx][ny] == 0:
                q.append((nx,ny,ncnt+1))
                visited[nx][ny] = 1
                
    

    


input = sys.stdin.readline

# dx = [1,2, 2, 1,-2,-1,-2,1]
# dy = [2,1,-1,-2,-1,-2,1,2]

T = int(input())

for _ in range(T):
    L = int(input())    
    visited = [[0]*L for _ in range(L)]
    A,B = map(int,input().split())    
    C,D = map(int,input().split())    
    print(bfs(A,B,C,D))