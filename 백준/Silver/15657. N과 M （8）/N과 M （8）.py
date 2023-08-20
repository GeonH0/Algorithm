

def dfs(n,s,tlst):
    if n == M:
        ans.append(tlst)
        return
    
    for j in range(s,N):
        dfs(n+1,j,tlst+[arr[j]])
        


N,M = map(int,input().split())

arr=list(map(int,input().split()))
arr.sort()
ans =[]

dfs(0,0,[])



for i in ans:
    print(*i)

