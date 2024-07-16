import sys
input = sys.stdin.readline

N = int(input())
arr = []
for _ in range(N):
    a = input().rstrip().split()    
    if a[0] == "push":
        arr.insert(0,int(a[1]))
    elif a[0] == "top":
        if len(arr) == 0:
            print(-1)
        else:
            print(arr[0])
    elif a[0] == "pop":
        if len(arr) == 0:
            print(-1)
        else:
            b = arr.pop(0)
            print(b)
    elif a[0] == "size":
        print(len(arr))
    elif a[0] == "empty":
        if len(arr) == 0:
            print(1)
        else:
            print(0)


    



    