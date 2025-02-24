
from collections import deque


def bfs(start,end):
    q = deque()
    q.append((start,0))
    v = [False] * 100001
    v[start] = True

    while q:
        cx,cnt = q.popleft()
        if cx == end:
            return cnt
        else:
            for i in (cx +1,cx-1,cx*2):
                if 0<=i <=100000 and not v[i]:
                    v[i] = True
                    q.append((i,cnt +1))
    



N,K = map(int,input().split())
print(bfs(N,K))
