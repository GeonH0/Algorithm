from random import randrange


def dfs_h(x,y):
    if x<= -1 or x>=n or y<=-1 or y>=m:
        return False
    if graph[x][y] == "-":

        
        graph[x][y]="x"

        dfs_h(x,y-1)
        
        dfs_h(x,y+1)

        return True
    return False

def dfs_v(x,y):
    if x<= -1 or x>=n or y<=-1 or y>=m:
        return False
    if graph[x][y]=='|':

        graph[x][y]='x'
        dfs_v(x-1,y)
        dfs_v(x+1,y)
        return True
    return False

n,m= map(int,input().split())
graph=[]
for _ in range(n):
    graph.append(list(input()))
cnt =0

for i in range(n):
    for j in range(m):
        if graph[i][j]=='-':
            dfs_h(i,j)
            cnt+=1
        elif graph[i][j]=='|':
            dfs_v(i,j)
            cnt +=1
print(cnt)