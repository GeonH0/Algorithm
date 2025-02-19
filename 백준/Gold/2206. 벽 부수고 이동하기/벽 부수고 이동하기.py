
from collections import deque


def bfs():
    q = deque()
    q.append((0,0,0,1))
    visited[0][0][0] = 1 # 시작점 방문 처리

    while q:
        cx,cy,broken,cnt = q.popleft()
        if cx == N-1 and cy == M-1:
            return cnt
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            
            if 0<=nx<N and 0 <= ny < M:
                # 벽이 아니고 방문 하지 않은 경우(벽을 부수지 않음)
                if arr[nx][ny] == '0' and visited[nx][ny][broken] == 0:
                    visited[nx][ny][broken] = 1
                    q.append((nx,ny,broken,cnt +1))
                # 벽이면서 아직 벽을 부수지 않은 경우
                if arr[nx][ny] == '1' and visited[nx][ny][1] == 0 and broken == 0:
                    visited[nx][ny][1] = 1
                    q.append((nx,ny,1,cnt +1))
    return -1
    


dx = [1,-1,0,0]
dy = [0,0,1,-1]

N,M = map(int,input().split())

arr = [list(input().strip()) for _ in range(N)]
visited = [[[0]*2 for _ in range(M)]for _ in range(N)] # 3차원으로 벽을 부쉈는지 여부를 포함시킨다.
print(bfs())