

N = int(input())
K = int(input())
arr = list(map(int,input().split()))
arr.sort()

if K>=N:
    print(0)
else:
    dist = []
    for i in range(1,N):
        dist.append(arr[i]-arr[i-1])

    dist.sort(reverse=True)

    for _ in range(K-1):
        dist.pop(0)
    print(sum(dist))