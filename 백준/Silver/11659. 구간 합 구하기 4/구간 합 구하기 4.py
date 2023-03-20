import sys
input = sys.stdin.readline

n,m = map(int,input().split())
arr=list(map(int,input().split()))
s_arr=[0]
temp=0
for i in arr:
    temp +=i
    s_arr.append(temp)

for _ in range(m):
    i,j = map(int,input().split())
    print(s_arr[j]-s_arr[i-1])
