import heapq


N = int(input())
heap = []
for _ in range(N):
    num = map(int,input().split())
    for n in num:
        heapq.heappush(heap,n)
        if len(heap)>N:
            heapq.heappop(heap)

print(heapq.heappop(heap))
