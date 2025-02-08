
def binary_search(lst,target,start,end):
    if start > end:
        return False
    mid = (start + end) // 2

    if lst[mid] == target:
        return True    
    elif lst[mid] > target:
        return binary_search(lst,target,start,mid-1)
    else:
        return binary_search(lst,target,mid+1,end)

N = int(input())
arr = list(map(int,input().split()))
M = int(input())
search = list(map(int,input().split()))

arr.sort()

for i in search:
    if binary_search(arr,i,0,len(arr)-1):
        print(1)
    else:
        print(0)