def dfs(n,sm,cnt):
    global ans
    #종료 조건, 정답관련 처리
    if n ==N:
        if sm == S and cnt>0:
            ans+=1
        return
    # 하부함수 호출
    #포함하는 경우, 포함하지 않는 경우
    dfs(n+1,sm+arr[n],cnt+1)
    dfs(n+1,sm,cnt)



N,S = map(int,input().split())
arr = list(map(int,input().split()))
ans = 0
dfs(0,0,0)
print(ans)