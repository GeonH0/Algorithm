from collections import deque


n,m = map(int,input().split())
mp=[list(input().strip())for _ in range(m)]


dx=[-1,1,0,0]
dy=[0,0,-1,1]

def bfs(x,y,color):
    q = deque()
    q.append((x,y))
    mp[x][y]=0

    cnt =1
    while q:
        x,y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
        
            if 0>nx or nx>=m or 0>ny or ny>=n:
                continue
            if mp[nx][ny] !=0 and  mp[nx][ny]==color:
                cnt+=1
                mp[nx][ny]=0
                q.append((nx,ny))
                
    return cnt

w,b=0,0
for i in range(m):
    for j in range(n):
        if mp[i][j]=='W':
            w+=(bfs(i,j,'W')**2)
        elif mp[i][j]=='B':
            b+=(bfs(i,j,'B')**2)
print(w,b)


