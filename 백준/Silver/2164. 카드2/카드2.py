


from collections import deque
import sys


input = sys.stdin.readline
N = int(input())

q = deque(range(1,N+1))

while len(q)>1:
    q.popleft()
    a = q.popleft()
    q.append(a)

print(q[0])
        
