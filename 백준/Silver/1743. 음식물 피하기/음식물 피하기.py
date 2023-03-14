import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline


n,m,k = map(int,input().split())
size =0
ans =0


graph = [[0]*(m+1) for _ in range(n+1)]


for _ in range(k):
    r,c = map(int,input().split())
    graph[r-1][c-1]=1

def dfs(x,y):
    global size
    if x<0 or x>n or y<0 or y>m:
        return False
    if graph[x][y]==1:
        size +=1
        graph[x][y]=0
        dfs(x+1,y)
        dfs(x-1,y)
        dfs(x,y+1)
        dfs(x,y-1)
        return True
    return False

for i in range(n):
    for j in range(m):
        if dfs(i,j) == True:
            ans = max(size,ans)
            size=0
print(ans)
