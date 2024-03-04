import sys
input = sys.stdin.readline

def round1(num):
    return int(num) + (1 if num - int(num) >= 0.5 else 0)

N = int(input())

if N:
    arr = []
    for _ in range(N):
        arr.append(int(input()))
    arr.sort()
    tmp = round1(N*0.15)
    print(round1(sum(arr[tmp:-tmp] if tmp else arr)/(N - 2 * tmp)))
else:
    print(0)







