
import sys


input = sys.stdin.readline

M,N = map(int,input().split())

arr = list(map(int,input().split()))

arr.sort()

start,end = 1,max(arr)
result = 0 

while start<= end:
    mid = (start + end)// 2
    total = sum(i//mid for i in arr)
    
    if total < M:
        end = mid - 1
    else:
        result = mid
        start = mid +1

print(result)