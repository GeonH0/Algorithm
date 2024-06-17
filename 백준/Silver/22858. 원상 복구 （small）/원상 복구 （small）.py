N,K = map(int,input().split())

S = list(map(int,input().split()))

D = list(map(int,input().split()))

ans = S

for i in range(K):
    tmp=list(range(N))
    for j in range(N):
        g = D[j]
        tmp[g-1] = ans[j]
    ans = tmp

print(*ans,end= ' ')
    

