
from collections import deque


def bfs(C):
    q = deque()
    q.append(C)
    ans_bfs.append(C)
    v[C] = 1
    while q:
        c = q.popleft()
        for i in arr[c]:
            if v[i] == 0:
                q.append(i)
                ans_bfs.append(i)
                v[i] = 1

def dfs(c):
    
    ans_dfs.append(c) # 정답 처리
    v[c] = 1 # 방문 표시

    for i in arr[c]:
        if v[i] == 0 :
            dfs(i)
    




N,M,V = map(int,input().split())
arr = [[] for _ in range(N+1)]

ans =[]
for _ in range(M):
    a,b = map(int,input().split())
    arr[a].append(b)
    arr[b].append(a)

for i in range(1,N+1):
    arr[i].sort()


v=[0]*(N+1)
ans_dfs= []
dfs(V)

v = [0]*(N+1)
ans_bfs= []
bfs(V)

print(*ans_dfs)  
print(*ans_bfs)  

