
def bfs(s,e):
    q =[]
    v=[0]*(N+1)
    
    q.append(s)
    v[s]=1

    while q:
        c = q.pop(0)
        #정답 처리
        if c== e:
            return v[c]-1

        for n in arr[c]:
            if not v[n]:
                q.append(n)
                v[n]+=v[c]+1
    return -1




N = int(input())
a,b = map(int,input().split())
M = int(input())
arr=[[] for _ in range(N+1)]
v=[0]*(N+1)

for _ in range(M):
    x,y = map(int,input().split())
    arr[x].append(y)
    arr[y].append(x)

ans = bfs(a,b)
print(ans)