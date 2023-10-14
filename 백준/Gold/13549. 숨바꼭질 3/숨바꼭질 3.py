from collections import deque

def bfs(s,e):
    q = deque()
    
    q.append(s)
    v[s]=0
    while q:
        c = q.popleft()
        if c == e:
            return v[c]
        else:
            for n in (c-1,c+1,c*2):
                if 0 <= n <= 100000 and v[n] == -1:
                    # 순간이동이라면
                    if n == c * 2:
                        v[n] = v[c] # 0초 추가 
                        q.appendleft(n) # 순간이동이기에 먼저 탐색

                    else: 
                        v[n] = v[c] + 1
                        q.append(n)

N,K = map(int,input().split())
v=[-1]*20000001
ans = bfs(N,K)
print(ans)
