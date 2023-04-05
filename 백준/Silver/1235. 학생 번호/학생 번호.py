


n = int(input())
arr=[]
cnt =0
for _ in range(n):
    arr.append(str(input()))


for i in range(1,len(arr[0])+1):
    ans =[]
    for j in range(n):
        if arr[j][-i:] in ans:
            break
        else:
            ans.append(arr[j][-i:])
            
    if len(ans) == n:
        print(i)
        break
    



