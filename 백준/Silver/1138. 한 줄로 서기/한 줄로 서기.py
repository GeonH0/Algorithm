import sys
input = sys.stdin.readline
n = int(input())
p =list(map(int,input().split()))

arr=[0]*n

for k in range(1,n+1):
    t = p[k-1]
    cnt =0
    for i in range(n):
        if cnt ==t and arr[i]==0:
            arr[i]=k
            break
        elif arr[i]==0:
            cnt +=1
print(*arr)
