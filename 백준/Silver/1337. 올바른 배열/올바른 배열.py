
n = int(input())
arr=[]
cnt =0
ans =[]
for _ in range(n):
    arr.append(int(input()))

arr.sort()
for i in range(0,n):
    cnt =0
    for j in range(arr[i],arr[i]+5):
        if j not in arr:
            cnt +=1
    ans.append(cnt)
print(min(ans))