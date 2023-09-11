
from collections import deque
import heapq


N = int(input())
q=[]
for _ in range(N):
    n = int(input())
    heapq.heappush(q,n)

cnt =0
while len(q)>1:
    x = heapq.heappop(q)
    y = heapq.heappop(q)
    cnt += (x+y)
    heapq.heappush(q,x+y)
print(cnt)