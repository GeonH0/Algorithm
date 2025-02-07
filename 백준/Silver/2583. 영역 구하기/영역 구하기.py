

from collections import deque


def bfs(x,y):
    q = deque()
    q.append((x,y))
    graph[x][y] = 1
    cnt = 1
    while q:
        cy,cx = q.popleft()
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if 0<= ny < M and 0<=nx<N and graph[ny][nx] == 0:               
                q.append((ny,nx))
                cnt +=1
                graph[ny][nx] = 1
    return cnt
                
        

M,N,K = map(int,input().split())

dx = [-1,1,0,0]
dy = [0,0,-1,1]

graph = [[0]*N for _ in range(M)]

for _ in range(K):
    lx,ly,rx,ry = map(int,input().split())
    for y in range(ly,ry):
        for x in range(lx,rx):
            graph[y][x] = 1 

ans = []            
for i in range(M):
    for j in range(N):
        if graph[i][j] == 0:
            ans.append(bfs(i,j))

ans.sort()
print(len(ans))
print(" ".join(map(str,ans)))