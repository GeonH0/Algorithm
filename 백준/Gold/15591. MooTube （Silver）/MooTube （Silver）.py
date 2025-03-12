from collections import deque
import sys

input = sys.stdin.readline

def bfs(start,k):
    q = deque()
    q.append(start)
    visited = [False] *(N+1)
    visited[start] = True
    cnt = 0
    while q:
        node = q.popleft()
        for n,u in arr[node]:
            if not visited[n] and u >= k:
                visited[n] = True
                q.append(n)
                cnt +=1
    return cnt

N,Q = map(int,input().split())
arr= [[]for _ in range(N+1)]
for _ in range(N-1):
    p,q,r = map(int,input().split())
    arr[p].append((q,r))
    arr[q].append((p,r))    


for _ in range(Q):
    k,v = map(int,input().split())
    print(bfs(v,k))
    
