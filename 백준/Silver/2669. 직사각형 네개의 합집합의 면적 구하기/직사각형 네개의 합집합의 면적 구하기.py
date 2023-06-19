arr=[[0]*100 for _ in range(100)]
cnt =0
for _ in range(4):
    x,y,a,b = map(int,input().split())

    for i in range(x,a):
        for j in range(y,b):
            if arr[i][j] ==0:
                arr[i][j]+=1
                cnt +=1
    
print(cnt)