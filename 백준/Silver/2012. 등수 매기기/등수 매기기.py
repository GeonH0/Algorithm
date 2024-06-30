import sys
input = sys.stdin.readline

N = int(input())
arr = [int(input()) for _ in range(N)]
arr.sort()

discrepancy = 0
for i in range(N):
    discrepancy += abs(arr[i] - (i + 1))

print(discrepancy)