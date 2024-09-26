import sys

input = sys.stdin.readline
N = int(input())
maps = input().strip()

cnt = 1
for i in range(1, N):
    if maps[i] != maps[i-1]:
        cnt += 1

print(cnt // 2)