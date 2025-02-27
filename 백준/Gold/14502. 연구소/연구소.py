from collections import deque
from itertools import combinations
import sys

input = sys.stdin.readline

# BFS로 바이러스 퍼뜨리기
def bfs():
    temp_arr = [row[:] for row in arr]  # 연구소 상태 복사
    q = deque(virus)  # 초기 바이러스 위치를 큐에 넣음

    while q:
        cx, cy = q.popleft()
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if 0 <= nx < N and 0 <= ny < M and temp_arr[nx][ny] == 0:
                temp_arr[nx][ny] = 2  # 바이러스 전파
                q.append((nx, ny))

    # 안전 영역 크기 계산
    return sum(row.count(0) for row in temp_arr)


# 벽 세우기 조합 생성
def build_walls():
    global max_safe_zone
    for walls in combinations(empty_spaces, 3):  # 가능한 벽 3개 조합을 생성
        for x, y in walls:
            arr[x][y] = 1  # 벽 세우기

        max_safe_zone = max(max_safe_zone, bfs())  # 안전 영역 최대값 갱신

        for x, y in walls:
            arr[x][y] = 0  # 벽 원상복구


# 입력 받기
N, M = map(int, input().split())
arr = []
virus = []  # 바이러스 위치 저장
empty_spaces = []  # 벽을 세울 수 있는 공간 저장

for i in range(N):
    row = list(map(int, input().split()))
    arr.append(row)
    for j in range(M):
        if row[j] == 2:
            virus.append((i, j))  # 바이러스 위치 저장
        elif row[j] == 0:
            empty_spaces.append((i, j))  # 벽을 세울 수 있는 위치 저장

# 4방향 탐색
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

max_safe_zone = 0  # 최대 안전 영역 저장

build_walls()  # 벽 세우기 시작

print(max_safe_zone)  # 정답 출력