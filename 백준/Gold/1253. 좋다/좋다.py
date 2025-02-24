
def tow_pointer(arr,target,index):
    left = 0 
    right = len(arr)-1
    while left< right:
        if left == index:
            left +=1
            continue
        if right == index:
            right -=1
            continue
        total = arr[left] + arr[right]
        if total == target:
            return True
        elif total <target:
            left +=1
        else:
            right -=1
    return False

N = int(input())

arr = list(map(int,input().split()))
ans = 0
arr.sort()

for i in range(N):
    if tow_pointer(arr,arr[i],i):
        ans +=1
print(ans)
