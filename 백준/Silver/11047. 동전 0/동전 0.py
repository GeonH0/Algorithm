
import sys


input = sys.stdin.readline

N,K = map(int,input().split())
arr = [int(input()) for _ in range(N)]
arr.sort(reverse=True)
j = 0
cnt = 0
for i in range(N):
    if K/arr[i] >=1:
        cnt += K//arr[i]
        K = K%arr[i]        
print(cnt)

