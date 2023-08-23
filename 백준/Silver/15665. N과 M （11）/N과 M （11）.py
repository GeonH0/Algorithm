


def dfs(n,lst):
    if n == M:
        ans.append(lst)
        return
    prev =0 
    for i in range(N):
        if prev != arr[i]:
            prev = arr[i]
            dfs(n+1,lst+[arr[i]])


N,M = map(int,input().split())
arr = list(map(int,input().split()))
arr.sort()
ans =[]
dfs(0,[])
for j in ans:
    print(*j)