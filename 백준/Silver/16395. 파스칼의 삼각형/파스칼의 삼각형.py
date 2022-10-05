n,k = map(int,input().split())

dp = []
for i in range(n):
    row = []
    for j in range(i+1):
        if j==0 or j==i:
            row.append(1)
        else:
            row.append(dp[i-1][j-1]+dp[i-1][j])
    dp.append(row)

print(f'{dp[n-1][k-1]}')