n = int(input())
arr = list(map(int,input().split()))
d = [1 for i in range(n)]

for i in range(n):
    for j in range(i):
        if arr[j] > arr[i]:
            d[i] = max(d[i],d[j]+1)

print(max(d))
    
    
