from collections import deque


def bfs(s,e):
    q = deque()
    v=[0] * 2000001
    q.append(s)
    # 시작점 방문처리
    
    v[s] = 1    
    while q:
        c = q.popleft()
        # 현재가 도착과 같으면 해당 위치를 찾은거기 때문에 해당 방문에서 -1
        #-1하는 이유는 처음 시작 visited가 1이기 때문
        if c == e:
            return v[c] - 1
        else:
            #아닐경우 3개의 가짓수를 돌면서
            for n in(c-1,c+1,c*2):
                #범위네에서 방문하지 않았다면
                if 0<=n<=200000 and v[n] ==0:
                    # Queue에 추가후
                    q.append(n)
                    # 방문 처리
                    v[n] = v[c]+1
    return -1

N,K = map(int,input().split())

ans = bfs(N,K)
print(ans)