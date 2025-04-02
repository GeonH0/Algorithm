
from collections import deque
import sys

input = sys.stdin.readline

def bfs(start,end):
    
    q = deque()
    q.append((start,1))
    visited = set()
    visited.add(start)
    while q:
        cur,cnt = q.popleft()
        if cur == end:
            return cnt
        for next in [cur*2,cur*10+1]:
            if next <= end and next not in visited:
                visited.add(next)
                q.append((next,cnt+1))
    return -1



A,B = map(int,input().split())


print(bfs(A,B))