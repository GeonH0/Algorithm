

N,M = map(int,input().split())

arr= [list(input().rstrip()) for _ in range(N)]

l = None
r = None

for i in range(N):
    if l != None:
        break
    for j in range(M):
        if arr[i][j] == "#":
            l = (i,j)
            break

for i in range(N-1,-1,-1):
    if r != None:
        break
    for j in range(M-1,-1,-1):
        if arr[i][j] == "#":
            r = (i,j)
            break
mid = ((l[0]+r[0])//2, (l[1]+r[1])//2)


if arr[l[0]][mid[1]] == ".":
    print("UP")
elif arr[mid[0]][l[1]] == ".":
    print("LEFT")
elif arr[mid[0]][r[1]] == ".":
    print("RIGHT")
elif arr[r[0]][mid[1]] == ".":
    print("DOWN")