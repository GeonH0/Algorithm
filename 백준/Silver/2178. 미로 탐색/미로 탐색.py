from collections import deque


def bfs(si,sj):
    q = deque()
    q.append((si,sj))

    v[si][sj] = 1

    while q:
        ci, cj = q.popleft()
        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nx, ny = dx + ci, dy + cj
            if 0 <= nx < N and 0 <= ny < M:
                if arr[nx][ny] == 0 or v[nx][ny] != 0:
                    continue
                v[nx][ny] = v[ci][cj] + 1
                q.append((nx, ny))



N,M  = map(int,input().split())
arr= []
v=[[0]*M for _ in range(N)]
for _ in range(N):
    arr.append(list(map(int,input().strip())))

bfs(0,0)
print(v[N-1][M-1])
