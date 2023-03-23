import sys
input = sys.stdin.readline

a,b = map(int,input().split())
m = int(input())
arr=list(map(int,input().split()))
arr.reverse()
ten =0
for i in range(m):
    ten += arr[i]*(a**i)
ans =[]
while ten//b:
    ans.append(ten%b)
    ten = ten//b
ans.append(ten)
ans.reverse()
for i in ans:
    print(i,end =" ")