
def binary_search(arr,target):
    start = 0
    end = len(arr) - 1
    while start <= end:
        mid = (start + end) //2
        if arr[mid] == target:
            return True
        if arr[mid] > target:
            end = mid -1
        else:
            start = mid +1

    return False
T = int(input())

for _ in range(T):
    N = int(input())
    note1 = list(map(int,input().split()))
    note1.sort()
    M = int(input())
    note2 = list(map(int,input().split()))
    for i in note2:
        if binary_search(note1,i):
            print(1)
        else:
            print(0)