

from collections import deque


def bfs(x,y,ex,ey):
    q = deque()
    v=[0]*N

    q.append((x,y))
    
    while q:

        cx,cy = q.popleft()
        #미방문 편의점 좌표를 범위내에 있는지 체크한다.
        if abs(cx-ex)+abs(cy-ey)<=1000: #목적지에 도달이 가능하다면 정답 처리
                        
            return 'happy'

        for i in range(N):
            if v[i]==0:
                nx,ny  = arr[i]
                if abs(cx-nx)+abs(cy-ny)<=1000: #범위 내에 있는것
                    q.append((nx,ny))
                    v[i]=1
                    
    return 'sad'
         






t = int(input())

for _ in range(t):
    N = int(input())
    si,sj = map(int,input().split())
    arr=[]
    
    for _ in range(N):
        arr.append(list(map(int,input().split())))
    ei,ej = map(int,input().split())
    ans = bfs(si,sj,ei,ej)
    print(ans)


