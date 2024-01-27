
import sys
input  = sys.stdin.readline
ans =[]
n = int(input())
for _ in range(n):
    arr = list(map(int,input().split()))
    if arr[0] == 1:
        ans.append(arr[1])
    elif arr[0] == 2:
        if ans:
            print(ans.pop())
        else:
            print(-1)
        
    elif arr[0] == 3:
        print(len(ans))
    elif arr[0] ==4:
        if ans :
            print(0)
        else:
            print(1)
    elif arr[0] == 5:
        if ans :
            print(ans[-1])
        else:
            print(-1)