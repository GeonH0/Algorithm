
from collections import deque


def melt():
    bing_cnt = [[0]*M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if arr[i][j] > 0: # 빙산이 있으면
                 for k in range(4): # 4방향 탐색
                    nx = i + dx[k]
                    ny = j + dy[k]
                    if 0<=nx<N and 0<=ny<M and arr[nx][ny] == 0:
                        bing_cnt[i][j] +=1
    
    # 빙하를 한꺼번에 다 녹여줌
    for i in range(N):
        for j in range(M):
            arr[i][j] -= bing_cnt[i][j]
            if arr[i][j] <0:
                arr[i][j] =0

            
def bfs(x,y,visited):
    q = deque()
    q.append((x,y))
    visited[x][y] = True

    while q:
        cx,cy = q.popleft()
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if 0<=nx<N and 0<=ny<M and not visited[nx][ny] and arr[nx][ny] > 0:
                visited[nx][ny] = True
                q.append((nx,ny))

                
def count_bing():
    visited =[[False]*M for _ in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(M):
            if arr[i][j] >0 and not visited[i][j]:
                bfs(i,j,visited)
                cnt +=1
                if cnt >=2:
                    return cnt
    return cnt

    

            

dx = [-1,1,0,0]
dy = [0,0,-1,1]                
    


N,M = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
year = 0  # 시간 (빙산이 녹는 년도)

while True:
    melt()  # 빙산이 한 번 녹음
    year += 1  # 1년 경과

    # 빙산 덩어리 개수 확인
    iceberg_count = count_bing()
    
    if iceberg_count == 0:
        print(0)
        break
    elif iceberg_count >= 2:
        print(year)
        break