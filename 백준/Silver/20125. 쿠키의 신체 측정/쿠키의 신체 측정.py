

N = int(input())
arr=[]
h = 0
hx = 0
hy = 0
leftarm = 0
rightarm = 0
leftleg = 0
rightleg = 0

for _ in range(N):
    arr.append(list(str(input())))

for i in range(N):
    for j in range(N):        
        if h == 0 and arr[i][j] == "*":
            h = 1        
            hx = i+2
            hy = j +1
            print(hx,hy)
            break
            

for i in range(hy-1):
    if arr[hx-1][i] == "*":
        leftarm +=1
for i in range(hy,N):
    if arr[hx-1][i] == "*":
        rightarm +=1

back = 0
line = 0
for i in range(hx,N):
    if arr[i][hy-1] == "*":
        back +=1
        line = i

for i in range(N-1,line, -1):
    if arr[i][hy-2] == "*":
        leftleg+=1

for i in range(N-1,line,-1):
    if arr[i][hy] == "*":
        rightleg +=1

print(leftarm,rightarm,back,leftleg,rightleg)
           