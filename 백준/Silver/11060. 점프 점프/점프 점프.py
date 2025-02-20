
from collections import deque
import sys


def bfs():
    q = deque()
    q.append((0,0)) # 현재 위치, 점프 횟수

    visited[0] = True

    while q:
        cx,cnt = q.popleft()

        if cx == N-1:
            return cnt
        for i in range(cx+1,min(cx+arr[cx]+1,N)): # 현재칸에서 갈수 있는 모든 범위 탐색
            if not visited[i]:
                visited[i] = True
                q.append((i,cnt+1))
    return -1



input = sys.stdin.readline

N = int(input())
arr = list(map(int,input().split()))
visited = [False] * N

print(bfs())