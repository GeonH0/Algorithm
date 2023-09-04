
from collections import deque


def bfs(cx,cy):
    q = deque()
    q.append((cx,cy))
    v=[[0]* 16 for _ in range(16)]
    v[cx][cy] = 1

    while q:
        ci,cj = q.popleft()
        if arr[ci][cj] ==3:
            return 1
        
        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ni, nj = ci + di, cj + dj
            #범위내, 방문하지 않아으며, 벽
            if 0 <= ni < 16 and 0 <= nj < 16 and   arr[ni][nj]!=1  and  v[ni][nj]==0  :
                q.append((ni,nj))
                v[ni][nj]= 1
    return 0



for test_case in range(1,11):
    n = int(input())
    arr= [list(map(int,input())) for _ in range(16)]
    si,sj = 0,0


    for i in range(16):
        for j in range(16):
            if arr[i][j]==2:
                si,sj = i,j
                
    ans = bfs(si,sj)
    print(f'#{test_case} {ans}')
    