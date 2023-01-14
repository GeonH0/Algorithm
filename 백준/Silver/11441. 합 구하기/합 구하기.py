import sys
input= sys.stdin.readline

n = int(input())
arr= list(map(int,input().split()))
cum =[arr[0]]
for i in range(1,n):
    cum.append(cum[-1]+arr[i])

m = int(input())
for _ in range(m):
    a,b= map(int,input().split())
    if a == 1:
        print(cum[b-1])
    else:
        print(cum[b-1]-cum[a-2])