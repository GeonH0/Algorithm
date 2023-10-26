


def dfs(ci,cj):

    if dp[ci][cj] == -1: #계산이 아직 안되있을 경우
        #4방향 더 높은 곳으로부터 낮은곳 방문시 경로수 누적
        dp[ci][cj] = 0 
        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            pi,pj = ci+di,cj+dj
            if arr[pi][pj] > arr[ci][cj]: #내리막일 경우
                dp[ci][cj] += dfs(pi,pj)

    return dp[ci][cj]
    


         




N,M = map(int,input().split())


arr=[[0]*(M+2)]+[[0] + list(map(int,input().split()))+[0] for _ in range(N)] +[[0]*(M+2)]

#dp 테이블 생성 및 초기값 설정
dp = [[-1]*(M+2) for _ in range(N+2)]
dp[1][1] = 1

print(dfs(N,M))


