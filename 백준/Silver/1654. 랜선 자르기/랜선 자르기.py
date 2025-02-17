

K,N = map(int,input().split())
arr = []

for _ in range(K):
    a = int(input())
    arr.append(a)

arr.sort()

result = 0
start,end = 1,max(arr)

while (start<=end):
    mid = (start+ end) // 2
    total = 0
    for i in arr:
        total += (i//mid)

    if total < N:
        end = mid - 1
    else:
        result = mid
        start = mid +1
print(result)