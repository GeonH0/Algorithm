from collections import deque

def bfs(si,sj,v,maps,N,M):
    q = deque()
    q.append((si,sj))
    v[si][sj]=1
    cnt = int(maps[si][sj])
    
    while q:
        ci,cj = q.popleft()
        
        #4방향, 범위내, 조건에 맞으면 실행
        for di,dj in ((-1,0),(1,0),(0,-1),(0,1)): #상, 하, 좌, 우
            ni,nj = ci+di,cj+dj
            #좌표가 범위안에 있고, X가 아니면서 방문하지 않았으면 다음으로
            if 0<=ni<N and 0<=nj<M and maps[ni][nj]!='X' and v[ni][nj]==0:
                q.append((ni,nj))
                v[ni][nj] =1
                cnt += int(maps[ni][nj])
    return cnt

        
    
    





def solution(maps):
    N,M = len(maps),len(maps[0])
    v=[[0]*M for _ in range(N)]
    answer = []
    for i in range(N):
        for j in range(M):
            if maps[i][j] !='X' and v[i][j]==0:
                answer.append(bfs(i,j,v,maps,N,M))
    
    
    
    
    if len(answer) !=0:
        return sorted(answer)
    
    else:
        return [-1]
    

