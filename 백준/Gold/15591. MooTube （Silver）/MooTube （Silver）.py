


from collections import deque


def bfs(k,v):
    vv=[0]*(N+1)
    q = deque()
    cnt =0

    q.append(v)
    vv[v]=1
    while q:
        c = q.popleft()
        for i in arr[c]:
            if vv[i[0]] ==0 and i[1]>=k:
                q.append(i[0])
                cnt +=1
                vv[i[0]]=1
    return cnt
                




N,Q = map(int,input().split())
arr=[[] for _ in range(N+1)]

for _ in range(N-1):
    x,y,r = map(int,input().split())
    arr[x].append((y,r))
    arr[y].append((x,r))
    

for _ in range(Q):
    k,v = map(int,input().split())
    print(bfs(k,v))
