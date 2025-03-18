
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(x):
    global cnt,cycle
    visited[x] = True # 방문처리
    next = arr[x]
    cycle.append(x)
    if visited[next]: # 만약 이미 방문한 노드라면
        if next in cycle: # 사이클이 형성된 경우
            cnt -= len(cycle[cycle.index(next):])
            return
    else:
        dfs(next)
    

T = int(input())
for _ in range(T):
    n = int(input())
    cnt = n
    cycle = []
    visited = [False] *(n+1)
    arr = [0] +list(map(int,input().split()))
    for i in range(1,n+1):
        if not visited[i]:
            cycle = []
            dfs(i)
    print(cnt)
