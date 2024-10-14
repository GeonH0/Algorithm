import sys
sys.setrecursionlimit(10000)

# 방향: 상, 하, 좌, 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def routeCheck(x, y):
    if x == M-1 and y == N-1:
        return 1  # 도착점에 도착한 경우 경로 1개 추가
    
    if dp[x][y] != -1:
        return dp[x][y]  # 이미 계산된 경로가 있으면 그 값 반환
    
    dp[x][y] = 0  # 아직 계산되지 않은 경우 경로를 0으로 초기화
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if 0 <= nx < M and 0 <= ny < N and arr[x][y] > arr[nx][ny]:
            dp[x][y] += routeCheck(nx, ny)  # 경로 탐색
    
    return dp[x][y]

M, N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(M)]
dp = [[-1] * N for _ in range(M)]  # 경로를 기록하는 dp 테이블

# 출발점에서 경로를 탐색 시작
print(routeCheck(0, 0))