
from collections import deque


def bfs(start,end):
    visited = [False] *100001
    q = deque()
    q.append((start,0))
    visited[start] = True

    while q:
        cx,cnt = q.popleft()
        if cx == end:            
            return cnt
        else:
            for i in (cx * 2, cx - 1, cx + 1):
                    if 0<=i <=100000 and not visited[i]:
                        visited[i] = True
                        if i == cx*2:                            
                            q.appendleft((i,cnt))
                        else:                            
                            q.append((i,cnt+1))




    


N,K = map(int,input().split())
print(bfs(N,K))