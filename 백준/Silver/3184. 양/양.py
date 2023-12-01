

from collections import deque


def bfs(ci,cj):
    q = deque()
    q.append((ci,cj))
    wolf = 0
    sheep =0
    #방문처리 및 양인지 늑대인지 체크
    if arr[ci][cj] == 'v':
        wolf +=1
    elif arr[ci][cj] == 'o':
        sheep += 1
    v[ci][cj] = 1 

    while q:
        x,y = q.popleft()
        for (di,dy) in ((1,0),(-1,0),(0,1),(0,-1)):
            ni,nj = di+x,dy+y
            if 0<=ni<R and 0<=nj<C:
                if v[ni][nj] == 0:
                    if arr[ni][nj] == '.':
                        q.append((ni,nj))
                        v[ni][nj] = 1
                    elif arr[ni][nj] == 'v':
                        wolf +=1
                        q.append((ni,nj))
                        v[ni][nj] = 1
                    elif arr[ni][nj] == 'o':
                        sheep +=1
                        q.append((ni,nj))
                        v[ni][nj] = 1
    if sheep ==0 and wolf ==0:
        return['None',0]
    elif sheep>wolf:
        return ['sheep',sheep]
    else:
        return ['wolf',wolf]
    



R,C = map(int,input().split())
arr = [list(map(str,input()))for _ in range(R)]
v=[[0]*C for _ in range(R)]
ans = [0,0]

for i in range(R):
    for j in range(C):
        if v[i][j] == 0:
            if arr[i][j] == '.' or arr[i][j] =='v' or arr[i][j] =='o':
                result = bfs(i,j)
                if result[0] == 'sheep':
                    ans[0] += result[1]
                elif result[0] =='wolf':
                    ans[1]+=result[1]
print(*ans)

