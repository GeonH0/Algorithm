




from collections import deque


def bfs(si,sj,v):
    q = deque()

    q.append((si,sj))
    v[si][sj]=1
    

    while q:
        ci,cj = q.popleft()
        # 4방향, 미방문, arr 값이 0보다 클경우
        for di,dj in ((-1,0),(1,0),(0,-1),(0,1)): #상, 하, 좌, 우
            ni,nj = ci+di,cj+dj
            if  arr[ni][nj] > 0 and v[ni][nj]==0:
                q.append((ni,nj))
                v[ni][nj] = 1
                





N,M = map(int,input().split())
arr=[list(map(int,input().split())) for _ in range(N)]
v=[[0]*M for _ in range(N)]


def solve():# 년, 전체순회 반복
    for y in range(1,90000):
        #4방향 0의 갯수 count
        a_sub = [[0]*M for _ in range(N)]
        # 가장자리는 제외하자
        for i in range(1,N-1):
            for j in range(1,M-1):
                if arr[i][j]==0:
                    continue
                for di,dj in((-1,0),(1,0),(0,-1),(0,1)):
                    ni,nj = i+di,j+dj
                    if arr[ni][nj]==0:
                        a_sub[i][j]+=1
        # 높이 낮추기
        for i in range(1,N-1):
            for j in range(1,M-1):
                if a_sub[i][j]>0:
                    arr[i][j]=max(0,arr[i][j]-a_sub[i][j])

        #빙산 덩어리 개수 count
        v=[[0]*M for _ in range(N)]
        cnt =0
        for i in range(1,N-1):
            for j in range(1,M-1):
                if v[i][j]==0 and arr[i][j]>0:
                    bfs(i,j,v)
                    cnt +=1
                    if cnt>1: # 덩어리 갯수 2 이상
                        return y
        #덩어리 갯수가 0이면 0으로 return 
        if cnt ==0:
            return 0

        

ans = solve()
print(ans)