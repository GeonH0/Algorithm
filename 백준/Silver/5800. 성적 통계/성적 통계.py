k = int(input())
cnt=0
for _ in range(k):    
    arr=list(map(int,input().split()))
    cnt =arr[0]
    arr.remove(cnt)
    arr.sort()
    m=[]
    for i in range(len(arr)-1):
        m.append(arr[i+1]-arr[i])

    print('Class',(_+1))
    print("Max %d, Min %d, Largest gap %d" %(arr[len(arr)-1],arr[0],max(m)))
