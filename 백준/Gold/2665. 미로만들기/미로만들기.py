from collections import deque
import heapq



def bfs(x,y):
    q= []
    heapq.heappush(q,(0,x,y))

    while q:
        cnt,cx,cy = heapq.heappop(q)
        v[cx][cy]=1

        if (cx,cy) ==(N-1,N-1):
            return cnt

        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ni, nj = cx + di, cy + dj

            if 0 <= ni < N and 0 <= nj < N and v[ni][nj]==0:
                v[ni][nj]=1
                if arr[ni][nj]==1:
                    heapq.heappush(q,(cnt,ni,nj))
                else:
                    heapq.heappush(q,(cnt+1,ni,nj))

        


N = int(input())

arr=[list(map(int,input().rstrip())) for _ in range(N)]
v=[[0]*N for _ in range(N)]
ans = bfs(0,0)
print(ans)
