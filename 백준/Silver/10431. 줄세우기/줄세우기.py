

T = int(input())

for _ in range(T):
    arr = list(map(int,input().split()))
    cnt = 0
    ans =[]
    for i in range(1,len(arr)-1):
        for j in range(i+1,len(arr)):
            if arr[i] > arr[j]: # i 가 크면
                arr[i],arr[j] = arr[j],arr[i]
                cnt +=1
    print(arr[0],cnt)

        

