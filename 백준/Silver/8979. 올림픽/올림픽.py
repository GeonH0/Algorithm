N,K = map(int,input().split())

arr = []

for _ in range(N):
    num,gold,sliver,bronze = map(int,input().split())
    arr.append((num,gold,sliver,bronze))

arr.sort(key = lambda x: (-x[1],-x[2],-x[3]))

rank = 1
same = 1

for i in range(N):
    if arr[i][0] == K:
        print(rank)
        break
    
    # 메달 순위가 같으면 rank 유지
    if i > 0 and arr[i][1:] == arr[i-1 ][1:]:
        same+= 1
    else:
        rank = i+1
        same = 1