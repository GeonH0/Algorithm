N = int(input())

dp = [0] * (N+1)
if N >= 2:
    dp[2] = 1

# N이 3 이상일 때 초기화
if N >= 3:
    dp[3] = 1
if N >= 4:
    for i in range(4,N+1):        
        dp[i] = dp[i-1] +1
        if i %2 ==0:
            dp[i] = min(dp[i],dp[i//2]+1)
        if i %3 ==0:
            dp[i] = min(dp[i],dp[i//3]+1)
print(dp[N])