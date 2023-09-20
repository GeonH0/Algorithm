


H,W,X,Y = map(int,input().split())
ans =[[0]*W for _ in range(H)]
arr=[]
for _ in range(H+X):
    arr.append(list(map(int,input().split())))



for i in range(H):
    for j in range(W):
        ans[i][j] = arr[i][j]

for i in range(X,H):
    for j in range(Y,W):
        ans[i][j] = arr[i][j] - ans[i-X][j-Y]
for i in range(H):
    for j in range(W):
        print(ans[i][j],end =" ")
    print("")