

def dfs(n,cnt):
    global ans
    if n == N:
        ans = max(ans,cnt)
        return
    if arr[n][0]<=0:
        dfs(n+1,cnt) # 현재 계란이 깨진 경우 
    else:
        flag = False
        for i in range(N):
            if n==i or arr[i][0]<=0:
                continue
            flag = True
            arr[n][0] -= arr[i][1]
            arr[i][0] -=arr[n][1]
            dfs(n+1,cnt +int(arr[n][0]<=0)+ int(arr[i][0]<=0))
            arr[n][0]+=arr[i][1]
            arr[i][0] += arr[n][1]
        if flag == False:
            dfs(n+1,cnt)





N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]

ans =0
dfs(0,0)
print(ans)