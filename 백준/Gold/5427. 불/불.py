
from collections import deque
import sys


def bfs_fire():
    while fire_queue:
        x,y = fire_queue.popleft()
        for i in range(4):
            nx = dx[i] + x
            ny= dy[i] + y
            if 0 <= nx < h and 0 <= ny < w: # 범위 체크
                if fire_time[nx][ny] == -1 and arr[nx][ny] == '.': # 아직 방문하지 않았으면서 벽이 아닐경우
                    fire_time[nx][ny] = fire_time[x][y] +1 # 시간을 1초 더한뒤
                    fire_queue.append((nx,ny)) # 큐에 넣기

def bfs_saggeun():
    while saggeun_queue:
        x,y,time = saggeun_queue.popleft()
        # 탈출 가능하다면 현재시각에 +1을 하여 탈출
        if x == 0 or x == h-1 or y == 0 or y == w-1:
            return time + 1
        
        for i in range(4):
            nx = dx[i] + x
            ny= dy[i] + y
            if 0 <= nx < h and 0 <= ny < w:
                if arr[nx][ny] == '.' and ans_time[nx][ny] == -1: # 벽이 아니고, 방문하지 않았으면
                    if fire_time[nx][ny] == -1 or fire_time[nx][ny] > time+1: # 불보다 먼저 도착하거나, 불이 아직 나지 않은 경우
                        ans_time[nx][ny] = time +1
                        saggeun_queue.append((nx,ny,time+1))
    return 'IMPOSSIBLE'

input = sys.stdin.readline

T = int(input())
dx = [-1,1,0,0]
dy = [0,0,-1,1]

for _ in range(T):
    w,h = map(int,input().split())
    arr = [list(map(str,input().strip())) for _ in range(h)]
    fire_queue = deque()
    saggeun_queue = deque()

    fire_time = [[-1]*w for _ in range(h)]
    ans_time = [[-1]*w for _ in range(h)]

    for i in range(h):
        for j in range(w):
            if arr[i][j] == '*':
                fire_queue.append((i,j))
                fire_time[i][j] = 0
            elif arr[i][j] == '@':
                saggeun_queue.append((i,j,0))
                ans_time[i][j] = 0
    bfs_fire()
    print(bfs_saggeun())
            
                



