from collections import deque

# cnt를 2로 제한하여 친구의 친구 까지만 제한
def bfs(arr,start):    
    q = deque()
    q.append((start,0))
    visited[start] = True
    cnt = 0  
    while q:        
        c,d = q.popleft()
        if d >= 2:
            continue
        for i in arr[c]:
            if not visited[i]:                
                q.append((i,d+1))
                visited[i] = True
                cnt +=1
    return cnt





n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (n+1)
visited[1] = True


if not graph[1]:
    print(0)
else:
    bfs(graph,1)
    print(sum(visited)-1)