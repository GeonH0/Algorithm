import sys
input = sys.stdin.readline

n,k = map(int,input().split())
arr=[]
for _ in range(n):
    arr.append(list(map(int,input().split())))

arr.sort(key = lambda x : (x[1],x[2],x[3]),reverse=True)

for i in range(n):
    if arr[i][0] == k:
        index = i
for j in range(n):
    if arr[index][1:] == arr[j][1:]:
        print(j+1)
        break