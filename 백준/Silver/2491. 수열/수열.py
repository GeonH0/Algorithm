





N = int(input())
arr=list(map(int,input().split()))
dp1,dp2= [1]*N,[1]*N
for i in range(N-1):
    if arr[i+1]>= arr[i]:
        dp1[i+1] +=dp1[i]
for i in range(N-1):
    if arr[i+1]<= arr[i]:
        dp2[i+1] +=dp2[i]
max1 = max(dp1)
max2 = max(dp2)
print(max(max1,max2))