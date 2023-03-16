from collections import deque


n,m = map(int,input().split())
graph=[[]for _ in range(n+1)]
check=[0]*(n+1)

for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

cnt =0
def bfs(v):
     q = deque()
     q.append(v)
     check[v]=1
     while q:
         v = q.popleft()
         for j in graph[v]:
             if check[j]==0:
                 check[j]=check[v]+1
                 q.append(j)

bfs(1)
m_num = max(check)
print(check.index(m_num),m_num-1,check.count(m_num))
