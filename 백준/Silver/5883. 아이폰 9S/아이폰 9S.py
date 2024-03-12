

N = int(input())
arr= []
for _ in range(N):
    arr.append(int(input()))
arrs = set(arr)
cnt = 1
ans = 1

for i in arrs:
    cnt = 1
    num = -1
    for j in range(N):
        if arr[j] != i:
            if num == -1:
                num = arr[j]
            else:
                if num == arr[j]:
                    cnt +=1
                else:
                    ans = max(ans,cnt)
                    num = arr[j]
                    cnt = 1
    ans = max(ans,cnt)
print(ans)
