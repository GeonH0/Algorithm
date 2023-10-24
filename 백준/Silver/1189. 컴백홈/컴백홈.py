






def dfs(X,Y,Distance):

    global cnt

    if Distance == K and Y == C-1 and X ==0:
        #도착지점 달성시
        cnt +=1
    else:
        arr[X][Y] == 'T'

        for dx,dy in ((-1,0),(1,0),(0,-1),(0,1)):
            nx,ny = X+dx,Y+dy
            if (0<=nx<R and 0<=ny< C and arr[nx][ny] == '.') :
                arr[nx][ny] = 'T'
                #가능할 경우 T로
                dfs(nx,ny,Distance+1)
                # 다시 탐색, 탐색 후 원위치
                arr[nx][ny] = '.'


            



R,C,K = map(int,input().split())

arr = [list(input().rstrip()) for _ in range(R)]

cnt = 0
arr[R-1][0] = 'T'

dfs(R-1,0,1)

print(cnt)

