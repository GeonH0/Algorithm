



from collections import deque


def bfs(x,y):

    q = deque()
    q.append((x,y))
    vv=[[0]*5 for _ in range(5)]

    vv[x][y]=1
    cnt =1
    while q:
        cx,cy = q.popleft()
        for dx,dy in ((-1,0),(1,0),(0,-1),(0,1)):
            nx,ny = dx+cx,cy+dy
            if 0<=nx<5 and 0<=ny<5 and vv[nx][ny]==0 and v[nx][ny]==1:
                q.append((nx,ny))
                vv[nx][ny]=1
                cnt +=1
    return cnt ==7 #cnt 가 7이면 true 7이 아니면 false
        



def check():
    for i in range(5):
        for j in range(5):
            if v[i][j]==1:
                return bfs(i,j)



def dfs(n,cnt,scnt):
    global ans
    if cnt >7:  #이미 7명이 넘으면 불가기 떄문에 return
        return
    if n == 25:
        if cnt == 7 and scnt >=4: # 학생수가 7명이고, 다솜파 학생수가 4명이상이면 인접해있는지 체크후 정답처리
            if check():
                ans +=1
        return
    #포함되는 경우
    v[n//5][n%5] = 1 #포함시킨후
    dfs(n+1,cnt+1,scnt+int(arr[n//5][n%5]=='S'))
    v[n//5][n%5] = 0 # 원상복구시키기
    #포함되지 않는 경우
    dfs(n+1,cnt,scnt)


    









arr=[]
ans =0
for _ in range(5):
    arr.append(input())

#학생번호,포함학생수, 다솜파 학생수
v=[[0]*5 for _ in range(5)] 
dfs(0,0,0)
print(ans)