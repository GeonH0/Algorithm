N = int(input())

dp = [-1] * (N + 1)  # 모든 값 -1로 초기화
dp[3] = 1  # 3kg 한 개
if N >= 5:
    dp[5] = 1  # 5kg 한 개

for i in range(6, N + 1):  # 6부터 N까지 계산
    if dp[i - 3] != -1:  # 3kg 봉지를 사용할 수 있다면
        dp[i] = dp[i - 3] + 1
    if dp[i - 5] != -1:  # 5kg 봉지를 사용할 수 있다면
        dp[i] = min(dp[i], dp[i - 5] + 1) if dp[i] != -1 else dp[i - 5] + 1

print(dp[N])