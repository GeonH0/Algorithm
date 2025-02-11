
import sys

sys.setrecursionlimit(10**6)

input = sys.stdin.readline

def dfs(arr,start,visited):
    for i in arr[start]:
        if not visited[i]:
            visited[i] = start
            dfs(graph,i,visited)

N = int(input())

graph = [[] for _ in range(N+1)]

for _ in range(N-1):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [0] * (N+1)
visited[1] = 1 # 1번은 루트 노드
dfs(graph,1,visited)

for j in range(2,N+1):
    print(visited[j])
