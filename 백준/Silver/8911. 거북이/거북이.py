n = int(input())

dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]


for _ in range(n):
    m = list(map(str,input().strip()))
    direction = 0

    min_x,min_y,max_x,max_y = 0,0,0,0

    nx,ny =0,0

    for i in m:
        if i =="F":
            nx += dx[direction]
            ny += dy[direction]
        elif i=="B":
            nx-=dx[direction]
            ny -=dy[direction]
        elif i =="L":
            if direction ==3:
                direction = 0
            else:
                direction +=1
        elif i =="R":
            if direction ==0:
                direction=3
            else:
                direction -=1

        min_x,min_y = min(min_x,nx),min(min_y,ny)
        max_x,max_y = max(max_x,nx),max(max_y,ny)
    print(abs(max_x-min_x) * abs(max_y-min_y))

