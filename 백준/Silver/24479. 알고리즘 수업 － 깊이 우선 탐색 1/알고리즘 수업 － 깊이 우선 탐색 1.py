import sys
sys.setrecursionlimit(150000)
    


def dfs(s):
    global cnt
    v[s]=cnt
    arr[s].sort()
    for i in arr[s]:
        if v[i]==0:
            cnt +=1
            dfs(i)




N,M,R = map(int,input().split())
arr=[[] for _ in range(N+1)]
v=[0]*(N+1)
cnt =1

for _ in range(M):
    x,y = map(int,input().split())
    arr[x].append(y)
    arr[y].append(x)

for i in range(N+1):
    arr[i].sort()

dfs(R)

for i in range(1,N+1):
    print(v[i])

    