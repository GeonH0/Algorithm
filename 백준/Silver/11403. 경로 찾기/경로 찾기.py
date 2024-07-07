


from collections import deque


def bfs(x):
    q = deque()    
    q.append(x)
    check = [0 for _ in range(N)]
    while q:
        c = q.popleft()

        for i in range(N):
            if check[i] == 0 and arr[c][i] ==1 :
                q.append(i)
                check[i] = 1
                v[x][i] = 1


N = int(input())
arr= []
v= [[0]* N for _ in range(N)]

for _ in range(N):
    arr.append(list(map(int,input().split())))


for i in range(0,N):
    bfs(i)

for i in v:
    print(*i)