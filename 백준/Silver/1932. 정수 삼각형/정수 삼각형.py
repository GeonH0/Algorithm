

N = int(input())
arr = []
cnt = 0

for _ in range(N):
    arr.append(list(map(int,input().split())))


for i in range(1,N):
    for j in range(i+1):
        # 0번째 항목은 아래의 0번째와 더한다.
        if j == 0:
            arr[i][j] += arr[i-1][j]
        #마지막 항목은 바로 아래의 마지막 항목과 더한다
        elif j == i:
            arr[i][j] += arr[i-1][j-1]
        # 그게 아닐경우 두 화살표중 더 큰 경우를 더한다.
        else:
            arr[i][j] += max(arr[i-1][j-1],arr[i-1][j])

print(max(arr[N-1]))

