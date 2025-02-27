
import sys

input = sys.stdin.readline

def find(parent,x):
    if parent[x] != x:
        parent[x] = find(parent,parent[x])
    return parent[x]

def union(parent,a,b):
    rootA = find(parent,a)
    rootB = find(parent,b)
    if rootA < rootB:
        parent[rootB] = rootA
    else:
        parent[rootA] = rootB

N  = int(input())
M = int(input())
arr = []
for _ in range(M):
    a,b,c = map(int,input().split())
    arr.append((c,a,b))

arr.sort()
parent = [i for i in range(N+1)]
total = 0
seleted_edge = 0

for cost,a,b in arr:
    if find(parent,a) != find(parent,b):
        union(parent,a,b)
        total += cost
        seleted_edge += 1
        if seleted_edge == N-1:
            break
print(total)

