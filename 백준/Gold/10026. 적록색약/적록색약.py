
from collections import deque


def bfs(si,sj):

    q = deque()
    q.append((si,sj))
    v[si][sj]=1
    while q:
        ci,cj = q.popleft()
        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ni, nj = ci + di, cj + dj
            # 범위내, 미방문, 현재 좌표와 다음 좌표가 같을경우
            if 0 <= ni < N and 0 <= nj < N and v[ni][nj]==0 and arr[ni][nj]== arr[ci][cj] :
                v[ni][nj]=1
                q.append((ni,nj))

    



N= int(input())
arr=[list(map(str,input())) for _ in range(N)]
v=[[0]*N for _ in range(N)]

# 적록색약 아닌 경우
cnt1 =0

for i in range(N):
    for j in range(N):
        if v[i][j] == 0:
            bfs(i,j)
            cnt1 +=1

# 적록색약인 경우 빨강을 찾을경우 초록으로 변경시킨다.

for i in range(N):
    for j in range(N):
        if arr[i][j] =='R':
            arr[i][j] ='G'

v=[[0]*N for _ in range(N)]
cnt2 =0
for i in range(N):
    for j in range(N):
        if v[i][j] == 0:
            bfs(i,j)
            cnt2 +=1


print(cnt1,cnt2)
