




def dfs(c,d):
    global found
    v[c]= 1
    
    #정답처리, 깊이가 5 이면
    if d == 5:
        found = True
        return 
        
    for j in arr[c]:
        if v[j]==0:
            v[j]= 1
            dfs(j,d+1)
    v[c]=0
                    
                               

    
    
    
N,M = map(int,input().split())
arr=[[] for _ in range(N)]
v=[0]*(N+1)
found = False

for _ in range(M):
    x,y = map(int,input().split())
    arr[x].append(y)
    arr[y].append(x)



for i in range(N):
    dfs(i,1)
    if found:
        break


if found:
    print(1)
else:
    print(0)
    

