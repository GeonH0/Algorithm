





N,M = map(int,input().split())

arr = list(map(int,input().split()))

start,end = max(arr),sum(arr)

while start<= end:
    mid = (start + end) //2
    cnt = 1 #블루레이 갯수
    current_sum = 0
    for l in arr:
        if current_sum + l > mid:
            cnt +=1
            current_sum = l
        else:
            current_sum +=l
    
    if cnt <=M:
        result = mid
        end = mid -1
    else:
        start = mid +1

print(result)
        
    