N = int(input())

arr = [list(input()) for _ in range(N)]
v = [list(input()) for _ in range(N)]
ans = [['.']*N for _ in range(N)]
dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]

for x in range(N):
    for y in range(N):
        if arr[x][y] == '.' and v [x][y] == 'x':
            cnt = 0

            for i in range(8):
                nx = x + dx[i]
                ny = y + dy[i]

                if nx <0 or ny<0 or nx>=N or ny >=N:
                    continue
                if arr[nx][ny] == "*":
                    cnt +=1
            ans[x][y] = cnt
        
        if arr[x][y] == "*" and v[x][y] == "x":
            for a in range(N):
                for b in range(N):
                    if arr[a][b] == "*":
                        ans[a][b] = "*"

                    
for i in range(N):
    for j in range(N):
        print(ans[i][j], end='')
    print()                