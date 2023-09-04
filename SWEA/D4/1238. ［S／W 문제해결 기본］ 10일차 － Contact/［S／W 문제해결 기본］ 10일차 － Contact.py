

from collections import deque


def bfs(s):

    q = deque()
    q.append(s)
    v =[0]*101

    v[s]=1
    cnt =s
    while q:
        c = q.popleft()
        if v[cnt]<v[c] or (v[cnt]== v[c] and cnt<c):
            cnt = c
        for i in cont[c]:
            if v[i]==0:
                q.append(i)
                v[i]=v[c]+1
                
    return cnt
    




for test_case in range(1,11):
    n,s = map(int,input().split())
    arr = list(map(int,input().split()))
    cont = [[] for _ in range(101)]
    for i in range(0,len(arr),2):
        cont[arr[i]].append(arr[i+1])
    

                
    ans = bfs(s)
    print(f'#{test_case} {ans}')
    