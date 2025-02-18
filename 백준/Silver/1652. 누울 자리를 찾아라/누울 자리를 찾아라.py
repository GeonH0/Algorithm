


    
    
        




N = int(input())

arr = [list(input().strip()) for _ in range(N)]

h = 0
v = 0

for i in range(N):
    cnt = 0
    for j in range(N):
        if arr[i][j] == '.':
            cnt +=1
        else:
            if cnt >=2:
                h +=1
            cnt = 0
    if cnt >=2:
        h +=1

for j in range(N):
    cnt = 0
    for i in range(N):
        if arr[i][j] == '.':
            cnt +=1
        else:
            if cnt >=2:
                v +=1
            cnt =0
    if cnt >=2:
        v +=1
print(h,v)

