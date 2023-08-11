

from collections import deque


def bfs():
    q = deque()
    v = [[set() for _ in range(C)] for _ in range(R)]
    cnt =1
    q.append((0,0,arr[0][0]))
    v[0][0].add(arr[0][0])

    
    while q:
        ci,cj,cv = q.popleft()
        cnt = max(cnt,len(cv))
        #4방향, 범위, 중복값이 아닌경우, 중복시퀀스
        for di,dj in ((1,0),(-1,0),(0,-1),(0,1)):
            ni,nj = ci+di,cj+dj

            if 0<=ni<R and 0<=nj<C and arr[ni][nj] not in cv and cv+arr[ni][nj] not in v[ni][nj]:
                q.append((ni,nj,cv+arr[ni][nj]))                
                v[ni][nj].add((cv+arr[ni][nj]))
            
    return cnt



    


R,C = map(int,input().split())
arr=[list(map(str,input())) for _ in range(R)]

ans = bfs()
print(ans)