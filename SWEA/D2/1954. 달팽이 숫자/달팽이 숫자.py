
T = int(input())

for t in range(1,T+1):
    N = int(input())
    dx= [0,1,0,-1]
    dy = [1,0,-1,0]
    arr = [[0]*N for _ in range(N)]
    cnt = 1

    x,y,cnt,dr = 0,0,1,0
    arr[x][y] = cnt
    cnt +=1

    while cnt <= N*N:
        nx,ny = x + dx[dr], y + dy[dr]
        if 0<=nx<N and 0<=ny<N and arr[nx][ny] == 0:
            x,y = nx,ny
            arr[x][y] = cnt
            cnt +=1
        else:
            dr = (dr+1) % 4
    print(f'#{t}')
    for lst in arr:
        print(*lst)

