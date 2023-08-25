


import heapq
import sys
INF = sys.maxsize

def dijkstra(s):
    heap  =[]
    v[s]=0
    heapq.heappush(heap,(0,s))

    while heap:
        c,n = heapq.heappop(heap)

        if v[n]<c:
            continue
        for nn,w in arr[n]:
            nc = c+w
            if nc< v[nn]:
                v[nn] = nc
                heapq.heappush(heap,(nc,nn))


V,E = map(int,input().split())
k = int(input())
arr=[[] for _ in range(V+1)]
v=[INF]*(V+1)

for _ in range(E):
    x,y,w = map(int,input().split())
    arr[x].append((y,w))
    
dijkstra(k)
for i in range(1,V+1):
    print("INF" if v[i]== INF else v[i])