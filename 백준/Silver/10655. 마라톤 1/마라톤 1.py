import math

N = int(input())
arr=[list(map(int,input().split())) for _ in range(N)]

cnt = [0]

#이전 것과의 거리차리 입력
for i in range(N-1):
    dist = abs(arr[i+1][0]- arr[i][0]) + abs(arr[i+1][1]- arr[i][1])
    cnt.append(dist)
ans = sum(cnt)
    
    

dis = 0
mdis = math.inf

#총거리에서 하나의 점이 빠지면 그 이전 이후 거리가 빠지는거 그값을 다시 계산
for i in range(1,N-1):
    dis = ans-(cnt[i] + cnt[i+1]) + abs(arr[i+1][0]- arr[i-1][0]) + abs(arr[i+1][1]- arr[i-1][1])
    mdis = min(mdis,dis)
print(mdis)