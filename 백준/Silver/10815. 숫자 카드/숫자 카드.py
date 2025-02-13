
def binary_search(arr,target):
    start = 0
    end = len(arr)- 1
    

    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == target:
            return True
        if arr[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return False
        
        
N = int(input())
card = list(map(int,input().split()))
card.sort()

M = int(input())
serach = list(map(int,input().split()))
ans = []
for i in serach:
    if binary_search(card,i):        
        ans.append(1)
    else:
        ans.append(0)

print(" ".join(map(str,ans)))