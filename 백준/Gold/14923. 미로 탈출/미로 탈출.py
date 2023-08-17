from collections import deque

def bfs(si, sj, ei, ej):
    q= deque()
    q.append((si,sj,0))
    v[si][sj][0] = 1
    while q:
        ci,cj,magic = q.popleft()
        if ci == ei and cj == ej:
            return v[ci][cj][magic]-1
            
        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ni, nj = ci + di, cj + dj
            if 0 <= ni < N and 0 <= nj < M and   arr[ni][nj]==0  and  v[ni][nj][magic]==0  :
                q.append((ni, nj,magic))
                v[ni][nj][magic] = v[ci][cj][magic] + 1
            
            elif 0 <= ni < N and 0 <= nj < M and not v[ni][nj][magic]  and  arr[ni][nj]==1  and not magic:
                q.append((ni, nj,magic+1))
                v[ni][nj][magic+1] = v[ci][cj][magic] + 1
                

    return -1
    



N, M = map(int, input().split())
cx, cy = map(int, input().split())
ex, ey = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
v = [[[0] * 2 for _ in range(M)] for _ in range(N)]
ans = bfs(cx-1,cy-1,ex-1,ey-1)
print(ans)
