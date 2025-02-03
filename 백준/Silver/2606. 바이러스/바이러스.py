
def dfs(graph,c,visited):
    visited[c] = True
    for i in graph[c]:
        if not visited[i]:
            dfs(graph,i,visited)


N = int(input())
M = int(input())

graph = [[] for _ in range(N+1)]
for _ in range(M):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
visited = [False] * (N+1)

dfs(graph,1,visited)
ans = sum(visited) -1
print(ans)