
import sys
input = sys.stdin.readline

t = int(input())

for i in range(t):
    n,m = map(int,input().split())
    
    t= [[]for _ in range(n+1)]

    for _ in range(m):
        a,b = map(int,input().split())
        t[a].append(b)
        t[b].append(a)
    
    visit=[0]*(n+1)

    def dfs(idx,cnt):
        visit[idx]=1
        for i in t[idx]:
            if visit[i] ==0:
                cnt = dfs(i,cnt+1)
        return cnt
    result = dfs(1,0)
    print(result)
    
