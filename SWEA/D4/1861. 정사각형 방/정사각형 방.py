from collections import deque


def bfs(si,sj):
    q= deque()
    ans =[]
    q.append((si,sj))
    v[si][sj]=1
    ans.append(arr[si][sj])
    

    while q:
        ci,cj = q.popleft()
        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ni, nj = ci + di, cj + dj
            if 0 <= ni < N and 0 <= nj < N and v[ni][nj]==0 and (abs(arr[ci][cj]-arr[ni][nj])==1) :
                q.append((ni,nj))
                v[ni][nj]=1
                ans.append((arr[ni][nj]))
    return min(ans),len(ans)



T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    arr=[list(map(int,input().split())) for _ in range(N)]
    v=[[0]*N for _ in range(N)]
    num,cnt =N*N,0
    for i in range(N):
        for j in range(N):
            if v[i][j]==0:
                tnum,tcnt =bfs(i,j)
                if cnt <tcnt or (cnt ==tcnt and num>tnum):
                    num,cnt = tnum,tcnt
    print(f'#{test_case} {num} {cnt}')
                


