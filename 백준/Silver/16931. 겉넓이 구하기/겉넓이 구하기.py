import sys
input = sys.stdin.readline

N,M  = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
side1 = 0 #왼쪽에서
side2 = 0 # 오른쪽에서
side3 = N*M #위 아래

for i in range(N):
    for j in range(M):
        if j == 0 : #맨앞
            side1 += arr[i][j]
        else:
            if arr[i][j] > arr[i][j-1]: # 다음 블록이 이전블록 보다 클경우 그 차이만큼 더해주기
                side1 += arr[i][j]-arr[i][j-1]
for i in range(M):
    for j in range(N):
        if j ==0 :
            side2 += arr[j][i]
        else:
            if arr[j][i] > arr[j-1][i]:
                side2 += arr[j][i] - arr[j-1][i]
print((side1+side2+side3)*2)