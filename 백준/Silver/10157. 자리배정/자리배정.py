c,r = map(int,input().split())
k = int(input())

if r*c <k:
    print(0)
else:
    di, dj = [1,0,-1,0],[0,1,0,-1]
    #상하 좌우를 1로 둘러쌈 -> 범위체크 필요 없어짐 
    arr = [[1]*(c+2)]+[[1]+[0]*c+[1] for _ in range(r)] + [[1]*(c+2)]
    ci,cj,dr = 1,1,0
    for n in range(1,k):
        arr[ci][cj] = n
        ni,nj = ci+di[dr],cj+dj[dr]
        if arr[ni][nj] ==0: #이동가능
            ci,cj = ni,nj
        else: #범위밖 or 이미 좌표가 있는 경우
                dr = (dr+1)%4
                ci,cj = ci+di[dr],cj+dj[dr]
    print(f'{cj} {ci}')





