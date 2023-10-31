





N,K = map(int,input().split())
sset = set() # 같은 동전값 중복제거
coin = []


for _ in range(N):
    sset.add(int(input()))

INF = K+1
dp = [INF] *(K+1)
dp[0] =0 

for coin in sset:
    for j in range(1,K+1):
        if j - coin >=0:
            dp[j] = min(dp[j],dp[j-coin]+1)

ans = dp[K]
if ans == INF:
    print(-1)
else:
    print(ans)            
