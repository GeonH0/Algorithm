import sys
input = sys.stdin.readline

N,M = map(int,input().split())

cnt = 0
if N == 0:
    print(0)
else:
    arr = list(map(int,input().split()))
    w = 0
    cnt = 1
    for i in arr:
        if i + w <= M:
            w +=i
        else:
            w = i
            cnt +=1
    print(cnt)