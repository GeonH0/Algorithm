
N,M = map(int,input().split())
arr = []
for _ in range(N):
    a = int(input())
    arr.append(a)


start,end = max(arr),sum(arr)

def can_withdraw(K):
    cnt = 1
    balance = K

    for m in arr:
        if balance < m:
            cnt +=1
            balance = K
        balance -= m
    
    return cnt<=M

while start <= end:
    mid = (start + end) // 2
    
    if can_withdraw(mid):
        result = mid
        end = mid -1
    else:
        start = mid +1


print(result)