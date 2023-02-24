n = int(input())
arr=[]
for _ in range(n):
    arr.append(list(map(str,input())))


res=[0,0]

for i in range(n):
    h,v = 0,0
    for j in range(n):
        if arr[i][j]=='.':
            h+=1
        else:
            h=0
        if h==2:
            res[0]+=1
        
        if arr[j][i]=='.':
            v +=1
        else:
            v=0
        if v==2:
            res[1]+=1


        
print(*res)