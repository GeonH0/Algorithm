
from collections import deque
import sys
input = sys.stdin.readline

def bfs(s,g):
    q = deque()
    q.append(s)    
    visited[s] = 0
    while q:
        cx = q.popleft()
        for i in range(2):
            nx = cx + dx[i]
            if 1<=nx <=F and visited[nx] == -1:
                visited[nx] = visited[cx] +1
                if nx == g:
                    return visited[nx]
                q.append(nx)
    return 'use the stairs'

F,S,G,U,D = map(int,input().split())
dx =[U,-D]
visited = [-1] * (F+1)
if S == G:
    print(0)
    sys.exit()
elif U == 0 and D ==0:
    print('use the stairs')
    sys.exit()
else:
    print(bfs(S,G))