
def dfs(n,s,lst):
    if n == M:
        ans.append(lst)
        return
    prev =0

    for i in range(s,N):
        if v[i]==0 and prev != arr[i]:
            prev = arr[i]
            v[i]=1
            dfs(n+1,i+1,lst+[arr[i]])
            v[i]=0





N,M = map(int,input().split())
arr = list(map(int,input().split()))
arr.sort()
ans = []
v=[0]*N
dfs(0,0,[])

for i in ans:
    print(*i)