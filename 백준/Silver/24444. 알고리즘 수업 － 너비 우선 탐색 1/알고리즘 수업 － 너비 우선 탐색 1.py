

from collections import deque

import sys
input = sys.stdin.readline


def bfs(s):
    global cnt
    q = deque()
    q.append(s)
    v[s]=1

    while q:
        c = q.popleft()
        for n in arr[c]:
            if v[n]==0:
                cnt +=1
                q.append(n)
                v[n]=cnt
            





N,M,R = map(int,input().split())

arr=[[] for _ in range(N+1)]
v=[0]*(N+1)
cnt=1

for _ in range(M):
    x,y = map(int,input().split())
    arr[x].append(y)
    arr[y].append(x)


for i in range(1,N):
    arr[i].sort()


bfs(R)

for i in v[1:]:
    print(i)