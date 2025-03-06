
from collections import deque
import sys


def bfs_fire():
    while fire_queue:
        x,y = fire_queue.popleft()
        for i in range(4):
            nx = dx[i] + x
            ny= dy[i] + y
            if 0 <= nx < R and 0 <= ny < C: # 범위 체크
                if fire_time[nx][ny] == -1 and arr[nx][ny] != '#': # 아직 방문하지 않았으면서 벽이 아닐경우
                    fire_time[nx][ny] = fire_time[x][y] +1 # 시간을 1초 더한뒤
                    fire_queue.append((nx,ny)) # 큐에 넣기

def bfs_jihoon():
    while jihun_queue:
        x,y,time = jihun_queue.popleft()
        # 탈출 가능하다면 현재시각에 +1을 하여 탈출
        if x == 0 or x == R-1 or y == 0 or y == C-1:
            return time + 1
        
        for i in range(4):
            nx = dx[i] + x
            ny= dy[i] + y
            if 0 <= nx < R and 0 <= ny < C:
                if arr[nx][ny] == '.' and ans_time[nx][ny] == -1: # 벽이 아니고, 방문하지 않았으면
                    if fire_time[nx][ny] == -1 or fire_time[nx][ny] > time +1: # 불보다 먼저 도착하거나, 불이 아직 나지 않은 경우
                        ans_time[nx][ny] = time +1
                        jihun_queue.append((nx,ny,time+1))
    return 'IMPOSSIBLE'
                


dx = [-1,1,0,0]
dy = [0,0,-1,1]
input = sys.stdin.readline

R,C =map(int,input().split())
fire_queue = deque()
jihun_queue = deque()

arr = [list(map(str,input().strip())) for _ in range(R)]
fire_time = [[-1]*C for _ in range(R)]
ans_time = [[-1]*C for _ in range(R)]

for i in range(R):
    for j in range(C):
        if arr[i][j] == "F":
            fire_queue.append((i,j))
            fire_time[i][j] = 0
        elif arr[i][j] == "J":
            jihun_queue.append((i,j,0)) # 지훈이 시작점
            ans_time[i][j] = 0

bfs_fire()
print(bfs_jihoon())