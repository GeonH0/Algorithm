H,W = map(int,input().split())
arr=[list(input().rstrip()) for _ in range(H)]
cnt =1
visited =False

for i in range(H):
    for j in range(W):

        if arr[i][j]=='c':
            arr[i][j]=0
            visited = True
            cnt =1

        elif arr[i][j]=='.' and visited==False: #바로전 구름이 없을겨우
            arr[i][j]= -1
        elif arr[i][j]=='.' and visited==True: # 바로전 구름이 있을경우
            arr[i][j]=cnt
            cnt +=1

    cnt =1
    visited=False
    print(*arr[i])





