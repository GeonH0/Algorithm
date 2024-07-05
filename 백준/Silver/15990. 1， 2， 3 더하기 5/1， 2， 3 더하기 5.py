
N = int(input())
dp = [[0 for _ in range(3)] for _ in range(100001)]
dp[1] = [1,0,0]
dp[2] = [0,1,0]
dp[3] = [1,1,1]
tmp = 1000000009
for i in range(4,100001):
    # 마지막 숫자가 1로 끝나야 하므로 n보다 1작은수 i-1의 값중 2와 3으로 끝나는 경우
    dp[i][0] = (dp[i-1][1] + dp[i-1][2])%tmp
    #2로 끝나야 하므로 i 보다 2작은수 중 1과 3으로 끝나는 경우의 합
    dp[i][1] = (dp[i-2][0] + dp[i-2][2])%tmp
    #3으로 끝나야 하므로 i 보다 3작은수 중 1과 2로 끝나는 경우
    dp[i][2] = (dp[i-3][0] + dp[i-3][1])%tmp

for _ in range(N):
    num = int(input())
    print(sum(dp[num])%tmp)