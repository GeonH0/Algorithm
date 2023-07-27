n  = int(input())
m = int(input())
arr =[[0]*n  for _ in range(n)]

x= (n-1)//2
y = (n-1)//2

#상, 하, 좌, 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
arr[x][y]=1

i = 2
start =3

while x!=0 or y!=0:
    while i<= start*start:
        if x== y==(n-1)//2: #시작점
            c_up,c_down,c_left,c_right = start,start-1,start-1,start-2
            x+=dx[0]
            y+=dy[0]
            c_up -=1
        elif c_right >0: #우
            x+=dx[3]
            y+=dy[3]
            c_right-=1        
        elif c_down>0:
            x+=dx[1]
            y+=dy[1]
            c_down-=1
        elif c_left>0:
            x+=dx[2]
            y += dy[2]
            c_left -=1


        elif c_up>0:
            x+=dx[0]
            y+=dy[0]
            c_up-=1
        arr[x][y]=i
        i+=1
    n-=2
    start+=2

for j in range(len(arr)):
    print(*arr[j])
    if m in arr[j]:
        mx = j+1
        my = arr[j].index(m) +1
print(mx,my)
