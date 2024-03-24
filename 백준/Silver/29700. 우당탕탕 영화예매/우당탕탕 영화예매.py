

N,M,P = map(int,input().split())
arr=[]
v= [[0]*M for _ in range(N)]
for _ in range(N):
    arr.append(list(map(int,input())))
res = 0
for i in range(N):
    check = 1
    for j in range(M):
        if arr[i][j] == 0:
            if check >= P:
                res +=1
            check+=1
        else:
            check = 1
print(res)
            

