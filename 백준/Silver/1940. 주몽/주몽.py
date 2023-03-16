


n = int(input( ))
m = int(input())

arr=list((map(int,input().split())))
arr.sort()
left,right = 0,len(arr)-1
cnt=0

while left<right:
    sum_num= arr[left]+arr[right]
    if sum_num<m:
        left+=1
    elif sum_num>m:
        right-=1
    else:
        cnt+=1
        left+=1
        right-=1
print(cnt)



