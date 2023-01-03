from tabnanny import check


def dfs(node):
    for n in graph[node]:
        if check[n]==0:
            check[n]=check[node]+1
            dfs(n)




n = int(input())
graph=[[]for _ in range(n+1)]
j,k = map(int,input().split())
for _ in range(int(input())):
    u,v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)
check=[0]*(n+1)
dfs(j)
print(check[k] if check[k]>0 else -1)