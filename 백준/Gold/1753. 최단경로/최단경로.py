

import heapq
import sys

input = sys.stdin.readline

V,E = map(int,input().split())
start = int(input())

INF = 1e9

graph = [[] for _ in range(V+1)]
distance = [INF] * (V+1)

for _ in range(E):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))


def dijkstar(start):
    q = []
    heapq.heappush(q,(0,start))
    distance[start] = 0
    while q:
        dist,now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))

dijkstar(start)

for i in range(1,V+1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])