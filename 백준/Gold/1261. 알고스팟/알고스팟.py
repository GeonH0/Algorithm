from collections import deque
import sys

input = sys.stdin.readline

M, N = map(int, input().split())  # 가로(M), 세로(N)
arr = [list(input().strip()) for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 벽을 부순 횟수를 저장하는 visited
visited = [[-1] * M for _ in range(N)]

def bfs():
    q = deque()
    q.append((0, 0))
    visited[0][0] = 0  # 시작점에서 벽 부순 횟수 0

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < M:
                # 아직 방문하지 않았거나, 더 적게 부수고 도달 가능하면
                if visited[nx][ny] == -1:
                    # 벽이 아니면 appendleft (우선 탐색)
                    if arr[nx][ny] == '0':
                        visited[nx][ny] = visited[x][y]
                        q.appendleft((nx, ny))
                    else:  # 벽이면 append
                        visited[nx][ny] = visited[x][y] + 1
                        q.append((nx, ny))

bfs()
print(visited[N - 1][M - 1])