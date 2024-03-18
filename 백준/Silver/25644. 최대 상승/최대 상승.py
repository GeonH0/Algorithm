




N = int(input())
arr = list(map(int,input().split()))
b,r  = 0,0

for i in range(N-1,-1,-1):
    b = max(b,arr[i])
    r = max(r,b-arr[i])
print(r)

