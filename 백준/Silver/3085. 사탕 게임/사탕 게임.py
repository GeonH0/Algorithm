

from re import search


N = int(input())
arr = [list(input().strip()) for _ in range(N)]

def search(arr):
    max_cnt = 0

    for i in range(N):
        cnt = 1
        for j in range(1,N):
            if arr[i][j] == arr[i][j-1]:
                cnt +=1
            else:
                cnt = 1
            max_cnt = max(cnt,max_cnt)
    for j in range(N):
        cnt = 1
        for i in range(1,N):
            if arr[i][j] == arr[i-1][j]:
                cnt +=1
            else:
                cnt =1
            max_cnt = max(cnt,max_cnt)
    return max_cnt


ans  = 0
for i in range(N):
    for j in range(N):
        if i < N-1 and arr[i][j] != arr[i+1][j]: # 위 아래 교환
            arr[i][j],arr[i+1][j] = arr[i+1][j],arr[i][j] # 교환
            ans = max(ans,search(arr)) # 탐색
            
            arr[i+1][j],arr[i][j] = arr[i][j],arr[i+1][j] # 원상 복구
        if j <N-1 and arr[i][j] != arr[i][j+1]:
            arr[i][j],arr[i][j+1] = arr[i][j+1],arr[i][j]
            ans = max(ans,search(arr))
            arr[i][j+1],arr[i][j] = arr[i][j],arr[i][j+1]
print(ans)