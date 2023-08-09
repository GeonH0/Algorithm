N = int(input())

arr=[]
def bfs(si,sj):
    q =[]
    q.append((si,sj))
    v[si][sj]=1 # 방문표시
    cnt =1 #정답 처리 관련 갯수
    while q:
        ci,cj = q.pop(0)
        for di,dj in ((-1,0),(1,0),(0,-1),(0,1)): #상, 하, 좌, 우
            ni,nj= ci+di,cj+dj
            if 0<=ni<N and 0 <=nj <N and arr[ni][nj]==1 and v[ni][nj]==0:
                q.append((ni,nj))
                v[ni][nj]= 1
                cnt +=1
    return cnt
        



for _ in range(N):
    arr.append(list(map(int,input())))

v=[[0]*N for _ in range(N)]
ans =[]


for i in range(N):
    for j in range(N):
        if arr[i][j]==1 and v[i][j]==0:
            ans.append(bfs(i,j))
ans.sort()
print(len(ans),*ans,sep='\n')

