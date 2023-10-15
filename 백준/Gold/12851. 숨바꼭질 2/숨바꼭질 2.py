

from collections import deque


def bfs1(s,e):
    q1 = deque()    
    q1.append(s)
    v[s]=1
    global cnt,path

    while q1:
        c = q1.popleft()
        
        if c == e:
            path = v[c]            
            cnt +=1
            continue
        else:
            for n in (c-1,c+1,c*2):
                if 0<=n<100001 and (v[n] == 0 or v[n] == v[c]+1):
                    v[n] = v[c] + 1
                    q1.append(n)
    



N,K = map(int,input().split())
v=[0]*100001

arr=[]
cnt,path = 0,0
ans = bfs1(N,K)
print(path-1)
print(cnt)
