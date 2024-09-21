
T = int(input())

for _ in range(T):
    N = int(input())
    arr = list(map(int,input().split()))
    Max =  -1000000
    Min =  1000000
    for i in arr:
        if i < Min:
            Min = i
        if i > Max:
            Max = i
    print(Min,Max)