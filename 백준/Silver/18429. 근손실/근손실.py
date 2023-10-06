





def dfs(k,w):
    global cnt 
    if w < 0:
        return
    if k >= N :
        cnt +=1
        return

    for i in range(N):
        if v[i] ==0:
            v[i] = 1
            dfs(k+1,w+arr[i]-K)
            v[i]=0



N, K = map(int, input().split())
arr = list(map(int, input().split()))

v =[0] * N
cnt =0
dfs(0,0)
print(cnt)
