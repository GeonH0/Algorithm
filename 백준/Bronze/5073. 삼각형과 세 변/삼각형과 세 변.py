
while True:    
    arr = list(map(int,input().split()))
    arr.sort(reverse= True)
    if arr[0] == 0 and arr[1] == 0 and arr[2] ==0:
        break
    if arr[0] >= arr[1] + arr[2]:
        print("Invalid")
        continue
    if arr[0] == arr[1] and arr[1] == arr[2] and arr[2] == arr[0]:
        print("Equilateral")
    elif arr[0] != arr[1] and arr[1] !=arr[2] and arr[0] !=arr[2]:
        print("Scalene")
    else:
        print("Isosceles")


