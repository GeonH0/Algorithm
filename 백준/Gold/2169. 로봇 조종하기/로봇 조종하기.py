N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

# dp[i][j]는 (i,j)까지 오는 최대 점수
dp = [[0] * M for _ in range(N)]

# 첫 번째 칸 초기화
dp[0][0] = arr[0][0]

# 첫 번째 행은 오른쪽으로만 갈 수 있음 (위/아래 없음)
for j in range(1, M):
    dp[0][j] = dp[0][j-1] + arr[0][j]

# 이후 각 행마다 처리
for i in range(1, N):
    # 왼쪽 → 오른쪽 방향 점수 저장
    left = [0] * M
    # 오른쪽 → 왼쪽 방향 점수 저장
    right = [0] * M

    # 왼쪽부터 오른쪽으로 (top-down)
    left[0] = dp[i-1][0] + arr[i][0]
    for j in range(1, M):
        left[j] = max(left[j-1], dp[i-1][j]) + arr[i][j]

    # 오른쪽부터 왼쪽으로 (bottom-up)
    right[M-1] = dp[i-1][M-1] + arr[i][M-1]
    for j in range(M-2, -1, -1):
        right[j] = max(right[j+1], dp[i-1][j]) + arr[i][j]

    # 현재 행의 dp 갱신: 왼쪽/오른쪽 중 큰 값 선택
    for j in range(M):
        dp[i][j] = max(left[j], right[j])

# 정답 출력
print(dp[N-1][M-1])