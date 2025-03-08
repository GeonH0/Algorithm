
def knapsack(N,K,itmes):
    dp = [[0]* (K+1) for _ in range(N+1)]
    for i in range(1,N+1):
        weight, value = itmes[i-1]
        for w in range(K+1):
            if weight > w: # 현재 물건을 넣을수 없는 경우
                dp[i][w] = dp[i-1][w]
            else:
                dp[i][w] = max(dp[i-1][w],dp[i-1][w-weight] + value)
    return dp[N][K]

n,k =map(int,input().split())
item = []
for _ in range(n):
    w,v = map(int,input().split())
    item.append((w,v))

print(knapsack(n,k,item))