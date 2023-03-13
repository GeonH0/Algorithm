n,m = map(int,input().split())
arr= list(map(int,input().split()))
arr1=list(map(int,input().split()))

arr.extend(arr1)
arr.sort()
for i in arr:
    print(i,end=" ")