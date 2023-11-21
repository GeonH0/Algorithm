


N = int(input())
arr = [0]+list(map(int,input().split()))



dp = [0]*(N+1)

for i in range(1,N+1):    
    for j in range(1,i+1):
        if dp[i] == 0 :
            dp[i] = dp[i-j] + arr[j]
        else:            
            dp[i] = min(dp[i],dp[i-j]+arr[j])

print(dp[N])