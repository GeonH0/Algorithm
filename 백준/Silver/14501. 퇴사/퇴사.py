import sys
input = sys.stdin.readline

def dfs(n,sm):
    global ans
    if n >= N: #종료 조건
        ans = max(ans,sm)
        return
    #상담하는 경우
    if n+ T[n] <=N:
        dfs(n+T[n],sm+P[n])

    #상담안 하는 경우
    dfs(n+1,sm)





N = int(input())
T = [0]*N
P =[0]*N
ans = 0
for i in range(N):
    T[i],P[i] = map(int,input().split())
dfs(0,0)
print(ans)