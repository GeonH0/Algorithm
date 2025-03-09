
import heapq
import sys

left_max_heap = []
right_min_heap = []



input = sys.stdin.readline

N = int(input())


for _ in range(N):
    num = int(input())

    if len(left_max_heap) == len(right_min_heap):
        heapq.heappush(left_max_heap,-num)
    else:
        heapq.heappush(right_min_heap,num)
    
    if right_min_heap and (-left_max_heap[0] > right_min_heap[0]):
        max_left = -heapq.heappop(left_max_heap)
        min_right = heapq.heappop(right_min_heap)

        heapq.heappush(left_max_heap, -min_right)
        heapq.heappush(right_min_heap,max_left)
    print(-left_max_heap[0])
    
    