


from collections import deque


def bfs(si,sj):
    q = deque()
    q.append((si,sj))
    
    v[si][sj]=0

    while q:
        ci,cj = q.popleft()
        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ni, nj = ci + di, cj + dj
            if 0 <= ni < N and 0 <= nj < M and v[ni][nj]==-1 :
                if arr[ni][nj]==0:
                    v[ni][nj]=0
                elif arr[ni][nj] ==1 :
                    v[ni][nj]= v[ci][cj]+1
                    q.append((ni,nj))
    return v
    


N,M = map(int,input().split())
arr=[list(map(int,input().split())) for _ in range(N)]
v=[[-1]*M for _ in range(N)]
for i in range(N):
    for j in range(M):
        if arr[i][j]==2 and v[i][j]==-1:
            bfs(i,j)
for i in range(N):
    for j in range(M):
        if arr[i][j]==0:
            print(0,end = ' ')
        else:
            print(v[i][j],end = ' ')
    print()