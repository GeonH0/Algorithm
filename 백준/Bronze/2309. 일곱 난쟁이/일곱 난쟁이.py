from doctest import REPORTING_FLAGS


arr=[]



def solve():
    N = 9
    num = sum(arr)-100
    for i in range(N-1):
        for j in range(i+1,N):
            if arr[i]+arr[j]== num:
                return arr[i],arr[j]

for _ in range(0,9):
    arr.append(int(input()))

n,m = solve()
for i in sorted(arr):
    if i!=n and i!=m:
        print(i)


        


