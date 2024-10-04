
N,M = map(int,input().split())

dp =[[0]*M for _ in range(N)]

cnt = 0
arr = [list(map(int,input().split())) for _ in range(N)]

# DP 배열을 순차적으로 업데이트하면서 최대 사탕 개수 계산
for i in range(N):
    for j in range(M):
        # 시작 위치 처리
        if i == 0 and j == 0:
            dp[i][j] = arr[i][j]
        else:
            # 위에서 오는 경우
            if i >  0:
                dp[i][j] = max(dp[i][j], dp[i-1][j] + arr[i][j])
            # 왼쪽에서 오는 경우
            if j > 0:
                dp[i][j] = max(dp[i][j], dp[i][j-1] + arr[i][j])
            # 대각선 위에서 오는 경우
            if i > 0 and j > 0:
                dp[i][j] = max(dp[i][j], dp[i-1][j-1] + arr[i][j])

# (N, M) 위치에서의 최대 사탕 개수를 출력
print(dp[N-1][M-1])
        
