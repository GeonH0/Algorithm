from collections import deque

def bfs(start, end):
    queue = deque()
    visited[start] = 0  # 시작 노드의 거리를 0으로 설정
    queue.append(start)
    
    while queue:
        current = queue.popleft()
        
        # 목표 노드(end)에 도달했다면 곧바로 반환해도 된다.
        if current == end:
            return visited[current]
        
        for neighbor in graph[current]:
            if visited[neighbor] == -1:  # 아직 방문되지 않은 노드
                visited[neighbor] = visited[current] + 1
                queue.append(neighbor)
    
    # while 문이 끝났는데도 도달하지 못하면 -1을 반환
    return -1
n = int(input())
a, b = map(int, input().split())
m = int(input())

graph = [[] for _ in range(n+1)]
for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)  # 양방향 연결

visited = [-1] * (n+1)  # -1로 초기화
result = bfs(a, b)

print(result)