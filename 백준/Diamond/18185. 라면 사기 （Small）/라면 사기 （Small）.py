

import sys


input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
cnt = 0
i = 0

while i < N:
    if i <= N-3 and arr[i+1] > arr[i+2]:
        # 2개 먼저 묶는게 더 이득인 경우
        m = min(arr[i], arr[i+1] - arr[i+2])
        cnt += 5 * m
        arr[i] -= m
        arr[i+1] -= m

    if i <= N-3:
        # 3개 묶을 수 있는 만큼 묶기
        m = min(arr[i], arr[i+1], arr[i+2])
        cnt += 7 * m
        arr[i] -= m
        arr[i+1] -= m
        arr[i+2] -= m

    if i <= N-2:
        # 2개 묶을 수 있는 만큼 묶기
        m = min(arr[i], arr[i+1])
        cnt += 5 * m
        arr[i] -= m
        arr[i+1] -= m

    # 남은거 단일 구매
    cnt += 3 * arr[i]
    arr[i] = 0

    i += 1

print(cnt)

                
                
                
                