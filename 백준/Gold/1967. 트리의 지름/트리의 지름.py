import sys
sys.setrecursionlimit(10**9)



def dfs(n,w):
    for i in arr[n]:
        x,y = i
        if v[x] == -1:
            v[x] = w+y
            dfs(x,w+y)



N = int(input())
arr=[[] for _ in range(N+1)]


cnt =0
for _ in range(N-1):
    x,y,z = map(int,input().split())
    arr[x].append((y,z))
    arr[y].append((x,z))

#1번 노드에서 가장 먼 곳 찾기
v = [-1]*(N+1)
v[1]=0
dfs(1,0)

#위에서 찾은 노드중 가장 먼 노드 찾기
start = v.index(max(v))
v = [-1]*(N+1)
v[start]=0
dfs(start,0)

print(max(v))