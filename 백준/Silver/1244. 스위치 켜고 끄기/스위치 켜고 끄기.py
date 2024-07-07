def change(a):
    if arr[a] == 0:
        arr[a] = 1
    else:
        arr[a] = 0
    return

N = int(input())
arr = list(map(int, input().split()))
T = int(input())

for _ in range(T):
    x, y = map(int, input().split())
    if x == 1:  # 남학생의 경우
        for i in range(y - 1, N, y):
            change(i)
    else:  # 여학생의 경우
        y -= 1
        change(y)
        for i in range(1, N // 2 + 1):
            if y - i < 0 or y + i >= N:
                break
            if arr[y - i] == arr[y + i]:
                change(y - i)
                change(y + i)
            else:
                break

for i in range(N):
    print(arr[i], end=' ')
    if (i + 1) % 20 == 0:
        print()