N = int(input())
cnt = {}
ans = 0
for _ in range(N):
    cow,dir = map(int,input().split())
    if cow in cnt:
        if dir == cnt[cow]:
            continue
        else:
            cnt[cow] = dir
            ans +=1
    else:
        cnt[cow] = dir
print(ans)