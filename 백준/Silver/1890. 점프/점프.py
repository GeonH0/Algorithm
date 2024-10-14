N = int(input())
arr = []
dp =[[0]*N for _ in range(N)]
for _ in range(N):
    arr.append(list(map(int,input().split())))

#dp[i][j]는 (0,0)에서 시작하여 i,j로 오는 경로수
dp[0][0] = 1

for i in range(N):
    for j in range(N):
        if dp[i][j] > 0  and arr[i][j] > 0:
            jump = arr[i][j]
            # 우측으로 이동
            if j + jump < N:
                dp[i][j+jump] += dp[i][j]
            # 아래로 이동
            if i +jump < N:
                dp[i+jump][j] += dp[i][j]

print(dp[N-1][N-1])
            
