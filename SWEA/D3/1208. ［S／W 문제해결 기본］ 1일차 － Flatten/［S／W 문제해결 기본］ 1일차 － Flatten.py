T = 10

for t in range(1,T+1):
    dump = int(input())
    arr = list(map(int,input().split())) 
    ans  = 100 
    for i in range(dump):
        arr.sort()
        arr[0] += 1
        arr[-1] -= 1
        if ans > max(arr) - min(arr):
            ans = max(arr)- min(arr)
    print(f'#{t} {ans}')

        