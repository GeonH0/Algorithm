


def dfs(n,s,lst):
    if n== M:
        ans.append(lst)
        return
    prev =0
    for i in range(s,N):
        if prev != arr[i]:
            prev = arr[i]
            dfs(n+1,i,lst+[arr[i]])
        


N,M  = map(int,input().split())
arr=list(map(int,input().split()))
arr.sort()
ans=[]
v=[0]*N

dfs(0,0,[])

for i in ans:
    print(*i)