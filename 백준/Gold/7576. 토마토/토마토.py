



from collections import deque


def bfs():

    q = deque()
    v=[[0]*M for _ in range(N)]

    cnt =0
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1:
                q.append((i,j))        
                v[i][j] =1
            elif arr[i][j]==0:
                cnt +=1
    while q:
        ci,cj = q.popleft()
        for di,dj in ((-1,0),(1,0),(0,-1),(0,1)): #상, 하, 좌, 우
            ni,nj = ci+di,cj+dj
            #좌표가 범위안에 있고, 미로가 1이면서 visited배열에 방문하지 않았으며 조건 충족
            if 0<=ni<N and 0<=nj<M  and v[ni][nj]==0 and arr[ni][nj]==0:
                q.append((ni,nj))
                v[ni][nj] = v[ci][cj]+1
                cnt -=1
    if cnt == 0:
        return v[ci][cj]-1
    else:
        return -1







M,N = map(int,input().split())

arr=[list(map(int,input().split())) for _ in range(N)]

ans = bfs()
print(ans)