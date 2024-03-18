M, n = map(int, input().split())
arr = [0, 0]
dir = 0

r = [0, -1, 0, 1]
c = [1, 0, -1, 0]
d = 0

for i in range(n):
    m, v = input().split()

    if m == "MOVE":
        arr[0] += c[dir] * int(v)  
        arr[1] += r[dir] * int(v)  
    else:
        if v == "0":  
            dir = (dir - 1) % 4  
        else:
            dir = (dir + 1) % 4  
    
    if not (0 <= arr[0] <= M and 0 <= arr[1] <= M):
        d = 1
        break

if d == 1:
    print(-1)
else:
    print(" ".join(map(str, arr)))
