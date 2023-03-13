from itertools import combinations


n,m = map(int,input().split())
arr=[]
for _ in range(n):
    arr.append(list(map(int,input().split())))
h =[]
c=[]

for i in range(n):
    for j in range(n):
        if arr[i][j]==1:
            h.append([i,j])
        elif arr[i][j]==2:
            c.append([i,j])

result = 1e9

for k in combinations(c,m):
    arr_d = 0
    for x in h:
        h_d=1e9
        for l in k:
            h_d=min(h_d, abs(x[0]-l[0])+abs(x[1]-l[1]))
        arr_d+=h_d
    result = min(result,arr_d)
print(result)
