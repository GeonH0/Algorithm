from collections import deque



n = int(input())

r1,c1,r2,c2 = map(int,input().split())

mp = [[0]*n for _ in range(n)]
dx=[-2,-2,0,0,2,2]
dy =[-1,1,-2,2,-1,1]


def bfs(x,y):
    q = deque()
    q.append((x,y))
    
    while q:
        x,y = q.popleft()
        for i in range(6):
            nx = x+dx[i]
            ny = y+dy[i]

            if 0<=nx<n and 0 <=ny<n and mp[nx][ny]==0:
                mp[nx][ny]=mp[x][y]+1
                if nx ==r2 and ny ==c2:
                    return mp[nx][ny]
                q.append((nx,ny))
    return -1

print(bfs(r1,c1))