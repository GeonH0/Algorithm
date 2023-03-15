import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline






def dfs(x,y):
    if x<=-1 or x>=m or y<=-1 or y>=n:
        return False
    if graph[x][y] ==1:

        graph[x][y]=0
        dfs(x+1,y)
        dfs(x+1,y+1)
        dfs(x+1,y-1)
        dfs(x-1,y)
        dfs(x-1,y+1)
        dfs(x-1,y-1)
        dfs(x,y+1)
        dfs(x,y-1)
        return True
    return False

m,n = map(int,input().split())

graph =[list(map(int,input().split())) for _ in range(m)]

r =0
for i in range(m):
    for j in range(n):
        if graph[i][j]==1:
            dfs(i,j)
            r+=1
print(r)