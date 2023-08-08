import sys
from typing import Deque
input = sys.stdin.readline

n = int(input())
q = Deque()

for i in range(n):
    b = list(map(str,input().split()))
    if b[0]=='push_back':
        q.append(b[1])
    elif b[0]=='push_front':
        q.appendleft(b[1])
    elif b[0]=='pop_back':
        if q:
            print(q.pop())
        else:
            print(-1)
    elif b[0]=='pop_front':
        if q:
            print(q.popleft())
        else:
            print(-1)
    elif b[0]=='size':
        print(len(q))
    elif b[0]=='empty':
        if q:
            print(0)
        else:
            print(1)
    elif b[0]=='front':
        if q:
            print(q[0])
        else:
            print(-1)
    elif b[0]=='back':
        if q:
            print(q[len(q)-1])
        else:
            print(-1)
        
        