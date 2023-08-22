


def dfs(n,lst):

    if n==M:
        ans.append(lst)
        return
    prev =0 
    for i in range(N):
        if v[i]==0 and prev != arr[i]:
            prev = arr[i]
            v[i]=1
            dfs(n+1,lst+[arr[i]])
            v[i]=0

N,M = map(int,input().split())
arr= list(map(int,input().split()))
arr.sort()
ans =[]
v=[0]*N
dfs(0,[])
ans.sort()
for i in ans:
    print(*i)

