

N,M = map(int,input().split())
arr = []
cnt = [0] * N
ans = []

for _ in range(N):
    arr.append(sorted(list(map(int,input().split()))))

for i in range(M):
    tmp=[]
    for j in range(N):
        tmp.append(arr[j][i])
    mx=max(tmp)
    for j in range(N):
        if mx==tmp[j]:
            cnt[j]+=1
winner=max(cnt)
for i in range(N):
    if cnt[i]==winner:
        ans.append(i+1)
print(*ans)
        
        
    
